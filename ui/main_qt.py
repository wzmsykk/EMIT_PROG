import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QEvent, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from .main_dlg import Ui_Dialog
from .sub_dlg_01_qt import SubDialog 
import pandas as pd
import numpy as np
from emittance.emit import emittance_calc_quadrupole,emittance_calc_solenoid
import matplotlib.pyplot as plt

class MainDialog(QDialog):

    def __init__(self, parent=None):

        super(QDialog, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags()	| Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint)
        self.sub = SubDialog()
        self.set_location_in_screen()
        self.sub.show()
        self._set_signal_slots()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.ui.frame_fig.setLayout(layout)
        self.model_quad=emittance_calc_quadrupole()
        self.model_sol=emittance_calc_solenoid()
    def set_location_in_screen(self):
        left_margin=5
        top_margin=5
        spacing=10
        ####SET PHASE VIEW DIALOG ON TOP LEFT
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget_phase= self.sub.geometry()
        x = left_margin
        y= top_margin
        self.sub.move(x, y)
        ####SET MAIN WINDOW ON TOP MIDDLE
        widget_main= self.geometry()
        x= widget_phase.width() + spacing 
        y= top_margin
        self.move(x, y)


        
        # widget = self.geometry()
        # x = ag.width() - widget.width()
        # y = 2 * ag.height() - sg.height() - widget.height()
        # self.move(x, y)
    def closeEvent(self, event):  # noqa:N802
        print("Main dialog close event")
        self.sub.close()
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                self.sub.showMinimized()
            else:
                self.sub.showNormal()
    def _set_signal_slots(self):
        self.ui.radioButton_quadrupole.clicked.connect(self.on_radioButton_quadrupole_clicked)
        self.ui.radioButton_solenoid.clicked.connect(self.on_radioButton_solenoid_clicked)
        self.ui.pushButton_calc.clicked.connect(self.calc)
        self.ui.pushButton_calc.setDefault(True)
        self.ui.pushButton_calck.clicked.connect(self.calck)
        pass
    def on_radioButton_quadrupole_clicked(self):
        self.ui.label_k.setText("聚焦参数K(m⁻²)")
        self.sub.ui.groupBox_quad.setEnabled(True)
        self.sub.ui.groupBox_sole.setEnabled(False)
        self.ui.radioButton_defocus.setEnabled(True)
    def on_radioButton_solenoid_clicked(self):
        self.ui.label_k.setText("聚焦参数K(m⁻¹)")
        self.sub.ui.groupBox_quad.setEnabled(False)
        self.sub.ui.groupBox_sole.setEnabled(True)
        self.ui.radioButton_focus.setChecked(True)
        self.ui.radioButton_defocus.setEnabled(False)
    def convert_line_to_list(self, line):
        l=[]
        for i in line.split(","):
            l.append(float(i.strip()))
        print(l)
        return l
    def covery_list_to_line(self, l,tail=3):
        fmtstr= "{:." + str(tail) + "f}"
        formatted_list = ', '.join([fmtstr.format(i) for i in l])
        return formatted_list
    def calck(self):
        ####GET TYPE
        mode=0
        if self.ui.radioButton_quadrupole.isChecked():
            mode=0
            c=self.model_quad
            print("quadrupole")
        elif self.ui.radioButton_solenoid.isChecked():
            print("solenoid")
            mode=1
            c=self.model_sol
        else:
            return
        try:
            c.energy=float(self.sub.ui.lineEdit_energy.text())
            print("energy",c.energy)
            if mode==0:
                c.L=float(self.sub.ui.lineEdit_quadL.text())
                print("Quad L",c.L)
                c.Ld=float(self.sub.ui.lineEdit_quadLd.text())
                print("Quad Ld",c.Ld)
            elif mode==1:
                c.L=float(self.sub.ui.lineEdit_soleL.text())
                print("Solenoid L",c.L)
                c.Ld=float(self.sub.ui.lineEdit_soleLd.text())
                print("Solenoid Ld",c.Ld)
            bdata=np.array(self.convert_line_to_list(self.ui.lineEdit_binput.text()))
            print("bdata",bdata)
            c.ks=c.b2k(bdata)
            print("ks",c.ks)
            self.ui.lineEdit_kinput.setText(self.covery_list_to_line(c.ks))
            print("success")
        except ValueError:
            return
        except AttributeError:
            return
    def calc(self):
        ####GET TYPE
        mode=0
        if self.ui.radioButton_quadrupole.isChecked():
            mode=0
            c=self.model_quad
        elif self.ui.radioButton_solenoid.isChecked():
            mode=1
            c=self.model_sol
        else:
            return
        try:
            c.energy=float(self.sub.ui.lineEdit_energy.text())
            print("energy",c.energy)
            if mode==0:
                c.L=float(self.sub.ui.lineEdit_quadL.text())
                print("Quad L",c.L)
                c.Ld=float(self.sub.ui.lineEdit_quadLd.text())
                print("Quad Ld",c.Ld)
            elif mode==1:
                c.L=float(self.sub.ui.lineEdit_soleL.text())
                print("Solenoid L",c.L)
                c.Ld=float(self.sub.ui.lineEdit_soleLd.text())
                print("Solenoid Ld",c.Ld)
            ks=np.array(self.convert_line_to_list(self.ui.lineEdit_kinput.text()))
            print(ks)
            sig2=np.array(self.convert_line_to_list(self.ui.lineEdit_sigma2.text()))
            print(sig2)
            if self.ui.radioButton_focus.isChecked():
                ef,ea,eb,ec,enx,ems=c.sol_f(ks,sig2)
            elif self.ui.radioButton_defocus.isChecked():
                ef,ea,eb,ec,enx,ems=c.sol_d(ks,sig2)
            print("Fitted parameters:", ef, ea, eb, ec, enx, ems)
        except ValueError:
            return
        except AttributeError:
            return
        
        
        
        betae,alphae,gammae=eb*ef,ea*ef,ec*ef
        if self.ui.radioButton_kvssigma2.isChecked():
            if self.ui.radioButton_focus.isChecked():
                fitted=[c.func_f(x,betae,alphae,gammae) for x in ks]
            elif self.ui.radioButton_defocus.isChecked():
                fitted=[c.func_d(x,betae,alphae,gammae) for x in ks]
            xlabel = 'K (m⁻²)' if self.ui.radioButton_quadrupole.isChecked() else 'K (m⁻¹)'
            ylabel = 'σ² (mm²)'
        elif self.ui.radioButton_bvssigma2.isChecked():
            try:
                bdata=np.array(self.convert_line_to_list(self.ui.lineEdit_binput.text()))
            except ValueError:
                return
            if self.ui.radioButton_focus.isChecked():
                fitted=[c.func_f(x,betae,alphae,gammae) for x in bdata]
            elif self.ui.radioButton_defocus.isChecked():
                fitted=[c.func_d(x,betae,alphae,gammae) for x in bdata]
            xlabel = 'B (T)' if self.ui.radioButton_solenoid.isChecked() else '∂B/∂x (T/m)'
            ylabel = 'σ² (mm²)'
        self.figure.clear()
        
        ax = self.figure.add_subplot(111)
        ax.plot(fitted, '*-')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.tight_layout()
        self.canvas.draw()
        
        self.ui.lineEdit_alpha.setText(str(ea))
        self.ui.lineEdit_beta.setText(str(eb))
        self.ui.lineEdit_gamma.setText(str(ec))
        self.ui.lineEdit_eps.setText(str(ef))
        self.ui.lineEdit_epsn.setText(str(enx))     

        
        