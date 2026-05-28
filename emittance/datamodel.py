
import datetime
import sys
from PyQt5 import QtCore,Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QHeaderView,QLabel
import numpy as np

class NumericAutoGrowModel(QAbstractTableModel):
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

    # === 优化 1：区分展示角色和编辑角色 ===
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
            
        row = index.row()
        col = index.column()
        val = self._data[row][col]

        # 界面文本展示
        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(val, float):
                return f"{val}"  # 浮点数展示
            if val == "":
                return ""
            return str(val)          # 整数或字符串直接转文本显示
            
        # 双击进入编辑状态时，返回原始数字（不带多余的0或格式化字符）
        if role == Qt.ItemDataRole.EditRole:
            return val

        # 视觉美化
        if role == Qt.ItemDataRole.BackgroundRole:
            if col == 1:
                return QColor("#f0fdf4")  # 计算列绿底
            if row == len(self._data) - 1 and self._data[row][0] == "":
                return QColor("#fafafa")  # 准备行灰底
                
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        if index.column() == 0 | index.column() == 2:
            return super().flags(index) | Qt.ItemFlag.ItemIsEditable
        return super().flags(index)

    # === 优化 2：智能识别输入类型并进行数学计算 ===
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if index.column() == 0 and role == Qt.ItemDataRole.EditRole:
            row = index.row()
            val_str = str(value).strip() # 确保转为字符串并去除空格
            
            # 如果清空了输入
            if val_str == "":
                self._data[row] = [""] * self.num_cols
                self.dataChanged.emit(index, self.index(row, self.num_cols - 1), [Qt.ItemDataRole.DisplayRole])
                return True
            
            # 【核心核心】尝试将输入的文本解析为 int 或 float
            try:
                if '.' in val_str:
                    parsed_val = float(val_str)  # 包含小数点存为 float
                else:
                    parsed_val = int(val_str)    # 不含小数点存为 int
            except ValueError:
                # 如果输入了字母、符号等非数字，返回 False，拒绝修改（表格会弹回原值）
                return False
                
            # 1. 将原生的数字类型写入数据源（此时存入的不再是字符串）
            self._data[row][0] = parsed_val
            
            # 2. 进行纯数字的联动计算（输出结果也是纯数字类型）
            self._data[row][1] = parsed_val * 13   # 结果通常为 int 或 float
            # self._data[row][2] = parsed_val / 2    # 结果必定为 float
            
            # 3. 自动增行
            if row == len(self._data) - 1:
                insert_row_idx = len(self._data)
                self.beginInsertRows(QModelIndex(), insert_row_idx, insert_row_idx)
                self._data.append([""] * self.num_cols)
                self.endInsertRows()

            self.dataChanged.emit(index, self.index(row, self.num_cols - 1), [Qt.ItemDataRole.DisplayRole])
            return True
            
        return False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datatest - 动态增行表格示例")
        self.resize(450, 400)

        # 初始数据（可以为空，也可以有初始值）
        headers = ["磁场梯度∂‌B/∂‌x(T/m)", "聚焦参数K(m⁻²)","束斑尺寸σ2 (mm2)"]
        initial_data = [
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
        self.model = NumericAutoGrowModel(initial_data, headers)
        self.table_view.setModel(self.model)
        
        # 优化表格拉伸样式
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.table_view.resizeColumnsToContents()
        # 提示标签
        label = QLabel("💡 提示：双击最后一行的空白单元格输入数字，回车后会自动计算并生成新行。")
        label.setStyleSheet("color: gray; padding: 5px;")

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())