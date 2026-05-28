
import datetime
import sys
from PyQt5 import QtCore,Qt
from PyQt5.QtGui import QColor,QKeySequence
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView,QLabel,QMenu,QShortcut
import numpy as np

class CompleteNumericModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers
        self.num_cols = len(self._headers)
        
        if not self._data or self._data[-1][0] != "":
            self._data.append([""] * self.num_cols)

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return self.num_cols

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        row, col = index.row(), index.column()
        val = self._data[row][col]

        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(val, float): return f"{val}"
            return "" if val == "" else str(val)
            
        if role == Qt.ItemDataRole.EditRole:
            return val

        if role == Qt.ItemDataRole.BackgroundRole:
            if col == 1: return QColor("#f0fdf4")
            if row == len(self._data) - 1 and self._data[row][0] == "": return QColor("#fafafa")
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            # 1. 横向表头（列名）
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            
            # 2. 纵向表头（行编号）
            if orientation == Qt.Orientation.Vertical:
                # 【UX小细节】如果是最后一行空白引导行，显示 "*" 号，模仿专业数据库操作
                if section == len(self._data) - 1 and self._data[section][0] == "":
                    return "*"
                # 普通行显示正常的行号：1, 2, 3...
                return str(section + 1)
                
        return None

    def flags(self, index):
        if not index.isValid(): return Qt.ItemFlag.NoItemFlags
        if index.column() == 0 or index.column() == 2: return super().flags(index) | Qt.ItemFlag.ItemIsEditable
        return super().flags(index)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if index.column() == 0 and role == Qt.ItemDataRole.EditRole:
            row = index.row()
            val_str = str(value).strip()
            
            if val_str == "":
                self._data[row] = [""] * self.num_cols
                self.dataChanged.emit(index, self.index(row, self.num_cols - 1), [Qt.ItemDataRole.DisplayRole])
                return True
            
            try:
                parsed_val = float(val_str) if '.' in val_str else int(val_str)
            except ValueError:
                return False
                
            self._data[row][0] = parsed_val
            self._data[row][1] = parsed_val * 13
            # self._data[row][2] = parsed_val / 2
            
            if row == len(self._data) - 1:
                insert_row_idx = len(self._data)
                self.beginInsertRows(QModelIndex(), insert_row_idx, insert_row_idx)
                self._data.append([""] * self.num_cols)
                self.endInsertRows()

            self.dataChanged.emit(index, self.index(row, self.num_cols - 1), [Qt.ItemDataRole.DisplayRole])
            return True
        return False

    # === 【核心增量 1】安全删除行的方法 ===
    def remove_custom_row(self, row):
        # 保护机制：如果选中的是最后一行（自动生成的空白准备行），不允许删除
        if row == len(self._data) - 1:
            return False
            
        # 通知视图：准备删除第 row 行
        self.beginRemoveRows(QModelIndex(), row, row)
        # 真正删除底层核心数据
        del self._data[row]
        # 通知视图：删除结束，视图会自动刷新并移除该行
        self.endRemoveRows()
        return True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataViewer")
        self.resize(450, 450)

        # 初始数据（可以为空，也可以有初始值）
        headers = ["磁场梯度∂‌B/∂‌x(T/m)", "聚焦参数K(m⁻²)","束斑尺寸σ2 (mm2)"]
        self.initial_data = [
            [0,20.4,0.03],
            [0,20.5,0.023],
            [0,20.6,0.017],
            [0,20.7,0.015],
            [0,20.8,0.0108],
            [0,20.9,0.009],
            [0,21,0.0086],
            [0,21.1,0.0093],
            [0,21.2,0.0114],
            [0,21.3,0.0144],
            [0,21.4,0.0185],
            [0,21.5,0.0228]
        ]

        self.table_view = QTableView()
        self.model = CompleteNumericModel(self.initial_data, headers)
        self.table_view.setModel(self.model)
        
        # 行列自适应与选择模式配置
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows) # 开启整行选中

        # === 【核心增量 2】策略一：右键菜单删除 ===
        # 开启自定义上下文菜单策略
        self.table_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self.show_context_menu)

        # === 【核心增量 3】策略二：键盘 Delete 键删除 ===
        self.shortcut_delete = QShortcut(QKeySequence(Qt.Key.Key_Delete), self.table_view)
        self.shortcut_delete.activated.connect(self.delete_selected_rows)

        # 界面布局
        label = QLabel("💡 提示：支持双击修改、输完自动加行。可以【右键点击行】或按【Delete键】删除行。")
        label.setStyleSheet("color: gray; padding: 5px;")
        
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 槽函数：弹出右键菜单
    def show_context_menu(self, pos):
        # 获取右键点击位置对应的行索引
        index = self.table_view.indexAt(pos)
        if index.isValid() and index.row() < self.model.rowCount() - 1: # 排除最后一行
            menu = QMenu(self)
            delete_action = menu.addAction("❌ 删除当前行")
            
            # 弹出菜单并等待点击
            action = menu.exec(self.table_view.viewport().mapToGlobal(pos))
            if action == delete_action:
                self.model.remove_custom_row(index.row())

    # 槽函数：处理 Delete 键（支持批量选中删除）
    def delete_selected_rows(self):
        # 获取所有选中的单元格/行索引
        select_model = self.table_view.selectionModel()
        selected_indexes = select_model.selectedRows() # 仅获取行索引，避免重复
        
        if not selected_indexes:
            return

        # 【关键算法】：必须将要删除的行号“从大到小（降序）”排序！
        # 比如你要删除第 1 行和第 2 行。如果先删第 1 行，原来的第 2 行就会变成新的第 1 行，导致行号错位。
        # 从后往前删（先删 2，再删 1）可以完美规避这个问题。
        rows_to_delete = sorted([idx.row() for idx in selected_indexes], reverse=True)
        
        for row in rows_to_delete:
            self.model.remove_custom_row(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())