import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from .main_dlg import Ui_Dialog
import pandas as pd
import numpy as np
from emittance.emit import emittance_calc_quadrupole,emittance_calc_solenoid
import matplotlib.pyplot as plt

class MainDialog(QDialog):

    def __init__(self, parent=None):

        super(QDialog, self).__init__(parent)

        self.ui = Ui_Dialog()

        self.ui.setupUi(self)

        self._set_signal_slots()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.ui.frame_fig.setLayout(layout)
    def _set_signal_slots(self):
        self.ui.radioButton_quadrupole.clicked.connect(self.on_radioButton_quadmag_clicked)
        self.ui.radioButton_solenoid.clicked.connect(self.on_radioButton_solenoid_clicked)
        self.ui.pushButton_calc.clicked.connect(self.calc)
        pass
    def on_radioButton_quadmag_clicked(self):
        self.ui.label_compname.setText("透镜(Q铁)有效长度L(m)")
        self.ui.radioButton_focus.setEnabled(True)
        self.ui.radioButton_defocus.setEnabled(True)
    def on_radioButton_solenoid_clicked(self):
        self.ui.label_compname.setText("线圈有效长度L(m)")
        self.ui.radioButton_focus.setChecked(True)
        self.ui.radioButton_defocus.setEnabled(False)
    def convert_line_to_list(self, line):
        l=[]
        for i in line.split(","):
            l.append(float(i.strip()))
        print(l)
        return l
    def calc(self):
        ####GET TYPE
        if self.ui.radioButton_quadrupole.isChecked():
            c=emittance_calc_quadrupole()
        elif self.ui.radioButton_solenoid.isChecked():
            c=emittance_calc_solenoid()
        else:
            return



        try:
            c.energy=float(self.ui.lineEdit_energy.text())
            print("energy",c.energy)
            c.L=float(self.ui.lineEdit_l.text())
            print("L",c.L)
            c.Ld=float(self.ui.lineEdit_ld.text())
            print("Ld",c.Ld)
            ks=np.array(self.convert_line_to_list(self.ui.lineEdit_kinput.text()))
            print(ks)
            sig2=np.array(self.convert_line_to_list(self.ui.lineEdit_sigma2.text()))
            print(sig2)
            if self.ui.radioButton_focus.isChecked():
                ef,ea,eb,ec,enx,ems=c.sol_f(ks,sig2)
            elif self.ui.radioButton_defocus.isChecked():
                ef,ea,eb,ec,enx,ems=c.sol_d(ks,sig2)
            print(ef,ea,eb,ec,enx,ems)
        except ValueError:
            return
        except AttributeError:
            return
        
        betae,alphae,gammae=eb*ef,ea*ef,ec*ef
        fittedf=[c.func_f(x,betae,alphae,gammae) for x in ks]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(fittedf, '*-')
        self.canvas.draw()
        
        self.ui.lineEdit_alpha.setText(str(ea))
        self.ui.lineEdit_beta.setText(str(eb))
        self.ui.lineEdit_gamma.setText(str(ec))
        self.ui.lineEdit_eps.setText(str(ef))
        self.ui.lineEdit_epsn.setText(str(enx))        
        