# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from pylab import *
import math
from pylab import *
from pykalman import UnscentedKalmanFilter
import time
from PyQt4 import QtCore, QtGui
from measurements_generation import *
from estimator_class import *
from PyQt4 import QtCore, QtGui
import imp

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global t,measurements_corrupted,measurements_filtered,measurements_pure      
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(984, 653)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 10, 961, 601))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.GenerateMes_tab = QtGui.QWidget()
        self.GenerateMes_tab.setObjectName(_fromUtf8("GenerateMes_tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 170, 121, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.gyr_accelero_edit_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.gyr_accelero_edit_layout.setObjectName(_fromUtf8("gyr_accelero_edit_layout"))
        self.gyro_noise_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.gyro_noise_edit.setObjectName(_fromUtf8("gyro_noise_edit"))
        self.gyr_accelero_edit_layout.addWidget(self.gyro_noise_edit)
        self.gyro_bias_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.gyro_bias_edit.setObjectName(_fromUtf8("gyro_bias_edit"))
        self.gyr_accelero_edit_layout.addWidget(self.gyro_bias_edit)
        self.acc_noise_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.acc_noise_edit.setObjectName(_fromUtf8("acc_noise_edit"))
        self.gyr_accelero_edit_layout.addWidget(self.acc_noise_edit)
        self.acc_bias_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.acc_bias_edit.setObjectName(_fromUtf8("acc_bias_edit"))
        self.gyr_accelero_edit_layout.addWidget(self.acc_bias_edit)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 71, 451))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.labels_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.labels_layout.setObjectName(_fromUtf8("labels_layout"))
        self.mag_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.mag_label.setObjectName(_fromUtf8("mag_label"))
        self.labels_layout.addWidget(self.mag_label, QtCore.Qt.AlignHCenter)
        self.gyro_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.gyro_label.setObjectName(_fromUtf8("gyro_label"))
        self.labels_layout.addWidget(self.gyro_label, QtCore.Qt.AlignHCenter)
        self.acc_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.acc_label.setObjectName(_fromUtf8("acc_label"))
        self.labels_layout.addWidget(self.acc_label, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(80, 60, 71, 91))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.mag_noise_label = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.mag_noise_label.setObjectName(_fromUtf8("mag_noise_label"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.mag_noise_label.addWidget(self.label_4, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(80, 220, 71, 91))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.gyr_noise_bias_label_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.gyr_noise_bias_label_layout.setObjectName(_fromUtf8("gyr_noise_bias_label_layout"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gyr_noise_bias_label_layout.addWidget(self.label_5, QtCore.Qt.AlignHCenter)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gyr_noise_bias_label_layout.addWidget(self.label_6, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(80, 340, 71, 141))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.acc_noise_bias_label_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.acc_noise_bias_label_layout.setObjectName(_fromUtf8("acc_noise_bias_label_layout"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.acc_noise_bias_label_layout.addWidget(self.label_7, QtCore.Qt.AlignHCenter)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.acc_noise_bias_label_layout.addWidget(self.label_8, QtCore.Qt.AlignHCenter)
        self.mag_noise_edit = QtGui.QLineEdit(self.GenerateMes_tab)
        self.mag_noise_edit.setGeometry(QtCore.QRect(150, 90, 121, 27))
        self.mag_noise_edit.setObjectName(_fromUtf8("mag_noise_edit"))
        self.duration_label = QtGui.QLabel(self.GenerateMes_tab)
        self.duration_label.setGeometry(QtCore.QRect(170, 10, 91, 17))
        self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName(_fromUtf8("duration_label"))
        self.time_edit = QtGui.QLineEdit(self.GenerateMes_tab)
        self.time_edit.setGeometry(QtCore.QRect(170, 30, 91, 27))
        self.time_edit.setObjectName(_fromUtf8("time_edit"))
        self.Generate_mes_pushButton = QtGui.QPushButton(self.GenerateMes_tab)
        self.Generate_mes_pushButton.setGeometry(QtCore.QRect(390, 10, 241, 21))
        self.Generate_mes_pushButton.setObjectName(_fromUtf8("Generate_mes_pushButton"))
        self.Import_pushButton = QtGui.QPushButton(self.GenerateMes_tab)
        self.Import_pushButton.setGeometry(QtCore.QRect(660, 10, 221, 21))
        self.Import_pushButton.setObjectName(_fromUtf8("Import_pushButton"))
        self.mesdata_comboBox = QtGui.QComboBox(self.GenerateMes_tab)
        self.mesdata_comboBox.setGeometry(QtCore.QRect(290, 40, 531, 31))
        self.mesdata_comboBox.setObjectName(_fromUtf8("mesdata_comboBox"))
        self.label = QtGui.QLabel(self.GenerateMes_tab)
        self.label.setGeometry(QtCore.QRect(40, 10, 41, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.fech_edit = QtGui.QLineEdit(self.GenerateMes_tab)
        self.fech_edit.setGeometry(QtCore.QRect(90, 10, 41, 27))
        self.fech_edit.setObjectName(_fromUtf8("fech_edit"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.GenerateMes_tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(290, 80, 661, 481))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.plotlayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.plotlayout.setObjectName(_fromUtf8("plotlayout"))
        self.plotbutton = QtGui.QPushButton(self.GenerateMes_tab)
        self.plotbutton.setGeometry(QtCore.QRect(840, 40, 99, 27))
        self.plotbutton.setObjectName(_fromUtf8("plotbutton"))
        self.tabs.addTab(self.GenerateMes_tab, _fromUtf8(""))
        self.estimators_tab = QtGui.QWidget()
        self.estimators_tab.setObjectName(_fromUtf8("estimators_tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.estimators_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 911, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.estimators_misc_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.estimators_misc_layout.setObjectName(_fromUtf8("estimators_misc_layout"))
        self.estimators_combobox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.estimators_combobox.setObjectName(_fromUtf8("estimators_combobox"))
        self.estimators_misc_layout.addWidget(self.estimators_combobox)
        self.estim_selec_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.estim_selec_button.setObjectName(_fromUtf8("estim_selec_button"))
        self.estimators_misc_layout.addWidget(self.estim_selec_button)
        self.import_estimator_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.import_estimator_button.setObjectName(_fromUtf8("import_estimator_button"))
        self.estimators_misc_layout.addWidget(self.import_estimator_button)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.estimators_tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 130, 194, 351))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.gains_vlayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.gains_vlayout.setObjectName(_fromUtf8("gains_vlayout"))
        self.Gain7layout = QtGui.QHBoxLayout()
        self.Gain7layout.setObjectName(_fromUtf8("Gain7layout"))
        self.label_Gain5 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain5.setObjectName(_fromUtf8("label_Gain5"))
        self.Gain7layout.addWidget(self.label_Gain5)
        self.edit_gain5 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain5.setObjectName(_fromUtf8("edit_gain5"))
        self.Gain7layout.addWidget(self.edit_gain5)
        self.gains_vlayout.addLayout(self.Gain7layout)
        self.Gain4layout = QtGui.QHBoxLayout()
        self.Gain4layout.setObjectName(_fromUtf8("Gain4layout"))
        self.label_Gain4 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain4.setObjectName(_fromUtf8("label_Gain4"))
        self.Gain4layout.addWidget(self.label_Gain4)
        self.edit_gain4 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain4.setObjectName(_fromUtf8("edit_gain4"))
        self.Gain4layout.addWidget(self.edit_gain4)
        self.gains_vlayout.addLayout(self.Gain4layout)
        self.Gain3layout = QtGui.QHBoxLayout()
        self.Gain3layout.setObjectName(_fromUtf8("Gain3layout"))
        self.label_Gain3 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain3.setObjectName(_fromUtf8("label_Gain3"))
        self.Gain3layout.addWidget(self.label_Gain3)
        self.edit_gain3 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain3.setObjectName(_fromUtf8("edit_gain3"))
        self.Gain3layout.addWidget(self.edit_gain3)
        self.gains_vlayout.addLayout(self.Gain3layout)
        self.Gain2layout = QtGui.QHBoxLayout()
        self.Gain2layout.setObjectName(_fromUtf8("Gain2layout"))
        self.label_Gain2 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain2.setObjectName(_fromUtf8("label_Gain2"))
        self.Gain2layout.addWidget(self.label_Gain2)
        self.edit_gain2 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain2.setObjectName(_fromUtf8("edit_gain2"))
        self.Gain2layout.addWidget(self.edit_gain2)
        self.gains_vlayout.addLayout(self.Gain2layout)
        self.Gain1layout = QtGui.QHBoxLayout()
        self.Gain1layout.setObjectName(_fromUtf8("Gain1layout"))
        self.label_Gain1 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain1.setObjectName(_fromUtf8("label_Gain1"))
        self.Gain1layout.addWidget(self.label_Gain1)
        self.edit_gain1 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain1.setObjectName(_fromUtf8("edit_gain1"))
        self.Gain1layout.addWidget(self.edit_gain1)
        self.gains_vlayout.addLayout(self.Gain1layout)
        self.Gain0layout = QtGui.QHBoxLayout()
        self.Gain0layout.setObjectName(_fromUtf8("Gain0layout"))
        self.label_Gain0 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_Gain0.setObjectName(_fromUtf8("label_Gain0"))
        self.Gain0layout.addWidget(self.label_Gain0)
        self.edit_gain0 = QtGui.QLineEdit(self.verticalLayoutWidget_7)
        self.edit_gain0.setObjectName(_fromUtf8("edit_gain0"))
        self.Gain0layout.addWidget(self.edit_gain0)
        self.gains_vlayout.addLayout(self.Gain0layout)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gains_vlayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.estimators_tab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(220, 120, 711, 251))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_Descr = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_Descr.setObjectName(_fromUtf8("label_Descr"))
        self.verticalLayout.addWidget(self.label_Descr)
        self.estim_description_plainTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_8)
        self.estim_description_plainTextEdit.setObjectName(_fromUtf8("estim_description_plainTextEdit"))
        self.verticalLayout.addWidget(self.estim_description_plainTextEdit)
        self.label_IC = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_IC.setObjectName(_fromUtf8("label_IC"))
        self.verticalLayout.addWidget(self.label_IC)
        self.IC_edit = QtGui.QLineEdit(self.verticalLayoutWidget_8)
        self.IC_edit.setObjectName(_fromUtf8("IC_edit"))
        self.verticalLayout.addWidget(self.IC_edit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.used_measurements_combobox = QtGui.QComboBox(self.verticalLayoutWidget_8)
        self.used_measurements_combobox.setObjectName(_fromUtf8("used_measurements_combobox"))
        self.horizontalLayout.addWidget(self.used_measurements_combobox)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.estimators_tab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(220, 400, 711, 131))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.actions_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.actions_layout.setObjectName(_fromUtf8("actions_layout"))
        self.run_button = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.actions_layout.addWidget(self.run_button)
        self.plot_button = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.plot_button.setObjectName(_fromUtf8("plot_button"))
        self.actions_layout.addWidget(self.plot_button)
        self.save_button = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.actions_layout.addWidget(self.save_button)
        self.tabs.addTab(self.estimators_tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabs.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabs.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.connect_mes_tab()
        self.connect_estim_tab()
        
        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.gyro_noise_edit.setText(_translate("MainWindow", "3", None))
        self.gyro_bias_edit.setText(_translate("MainWindow", "2", None))
        self.acc_noise_edit.setText(_translate("MainWindow", "1", None))
        self.acc_bias_edit.setText(_translate("MainWindow", "2", None))
        self.mag_label.setText(_translate("MainWindow", "Mag", None))
        self.gyro_label.setText(_translate("MainWindow", "Gyro", None))
        self.acc_label.setText(_translate("MainWindow", "Accelero", None))
        self.label_4.setText(_translate("MainWindow", "Noise:", None))
        self.label_5.setText(_translate("MainWindow", "Noise:", None))
        self.label_6.setText(_translate("MainWindow", "Bias:", None))
        self.label_7.setText(_translate("MainWindow", "Noise:", None))
        self.label_8.setText(_translate("MainWindow", "Bias:", None))
        self.mag_noise_edit.setText(_translate("MainWindow", "2", None))
        self.duration_label.setText(_translate("MainWindow", "Duration (s)", None))
        self.time_edit.setText(_translate("MainWindow", "10", None))
        self.Generate_mes_pushButton.setText(_translate("MainWindow", "Generate", None))
        self.Import_pushButton.setText(_translate("MainWindow", "Import", None))
        self.label.setText(_translate("MainWindow", "fech", None))
        self.fech_edit.setText(_translate("MainWindow", "50", None))
        self.plotbutton.setText(_translate("MainWindow", "Plot", None))
        self.tabs.setTabText(self.tabs.indexOf(self.GenerateMes_tab), _translate("MainWindow", "Generate Mes.", None))
        self.estim_selec_button.setText(_translate("MainWindow", "Select Estimator", None))
        self.import_estimator_button.setText(_translate("MainWindow", "Import estimator", None))
        self.label_Gain5.setText(_translate("MainWindow", "G0", None))
        self.edit_gain5.setText(_translate("MainWindow", "1", None))
        self.label_Gain4.setText(_translate("MainWindow", "G1", None))
        self.edit_gain4.setText(_translate("MainWindow", "1", None))
        self.label_Gain3.setText(_translate("MainWindow", "G2", None))
        self.edit_gain3.setText(_translate("MainWindow", "1", None))
        self.label_Gain2.setText(_translate("MainWindow", "G3", None))
        self.edit_gain2.setText(_translate("MainWindow", "1", None))
        self.label_Gain1.setText(_translate("MainWindow", "G4", None))
        self.edit_gain1.setText(_translate("MainWindow", "1", None))
        self.label_Gain0.setText(_translate("MainWindow", "G5", None))
        self.edit_gain0.setText(_translate("MainWindow", "1", None))
        self.pushButton.setText(_translate("MainWindow", "Save Gains", None))
        self.label_Descr.setText(_translate("MainWindow", "Description:", None))
        self.estim_description_plainTextEdit.setPlainText(_translate("MainWindow", "Let there be drones...", None))
        self.label_IC.setText(_translate("MainWindow", "Initial Cond.", None))
        self.IC_edit.setText(_translate("MainWindow", "zeros(9)", None))
        self.label_2.setText(_translate("MainWindow", "   used measurements", None))
        self.run_button.setText(_translate("MainWindow", "Run", None))
        self.plot_button.setText(_translate("MainWindow", "Plot", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.tabs.setTabText(self.tabs.indexOf(self.estimators_tab), _translate("MainWindow", "Def. Estimator", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("MainWindow", "Plot Estimation", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Optimizer", None))


    def connect_mes_tab(self):
        self.mescomboboxlist=[self.mesdata_comboBox,self.used_measurements_combobox]
        self.indexchangecounter=0
        self.Generate_mes_pushButton.clicked.connect(self.wrapper_gen_measurements)
        self.plotbutton.clicked.connect(self.wrapper_plot_to_graphic)
    
    #TAB 1 FUNC
    def wrapper_gen_measurements(self):
        global t,measurements_corrupted,measurements_filtered,measurements_pure        
        d=eval(self.time_edit.text())
        f=eval(self.fech_edit.text())
        mn=eval(self.mag_noise_edit.text())
        gn=eval(self.gyro_noise_edit.text())
        gb=eval(self.gyro_bias_edit.text())
        an=eval(self.acc_noise_edit.text())
        ab=eval(self.acc_bias_edit.text())
          
        gen_measurements(self,self.mescomboboxlist,d,f,an,gn,mn,ab,gb) 
        return
        
    def wrapper_plot_to_graphic(self):
        global fig
        cdata=self.mesdata_comboBox.currentText()
        data=eval("self."+cdata)
        plot_to_graphic(data,self.t)
        show()
        draw()
        return
        
       
    def connect_estim_tab(self):
        self.chosenestim=None
        self.currentoutput=None
        self.estim_list=[]
        
        self.gainslabellist=[eval("self.label_Gain"+str(i)) for i in range(6)]
        
        self.gainsfieldslist=[eval("self.edit_gain"+str(i)) for i in range(6)]
        
        self.import_estimator_button.clicked.connect(self.wrapper_import_estimator)
        self.estim_selec_button.clicked.connect(self.wrapper_select_estimator)
        self.run_button.clicked.connect(self.wrapper_run_estimator)        
        self.plot_button.clicked.connect(self.wrapper_plot_est_output)        
        
    def wrapper_import_estimator(self):
        p=QtGui.QFileDialog.getOpenFileNames()[0]
        
        #Car sinon il y a un u devant, no comprende porqe
        foo = imp.load_source('estimator', p)
        self.estim_list.append(foo.def_estim())
        self.estimators_combobox.addItem(self.estim_list[-1].name)
        self.wrapper_select_estimator()
    
    def wrapper_select_estimator(self):
        
        getestimatorname=self.estimators_combobox.currentText()
        for i in self.estim_list:
            if getestimatorname==i.name:
                self.chosenestim=i
                
        for i in range(len(self.gainsfieldslist)):
            if i<min(len(self.gainsfieldslist),len(self.chosenestim.gains_name)):
                self.gainslabellist[i].setText(self.chosenestim.gains_name[i])
                self.gainsfieldslist[i].setText(str(self.chosenestim.gains[i]))
            else:
                for k in self.gainslabellist[i:]:
                    k.setText("NA")
                for k in self.gainsfieldslist[i:]:
                    k.setText("NA")
                    
        self.estim_description_plainTextEdit.setPlainText(self.chosenestim.description)
        self.IC_edit.setText(str(self.chosenestim.initial_state))
    
    def wrapper_run_estimator(self):

        ic=eval(self.IC_edit.text())

        self.wrapper_gen_measurements() 
        self.chosenestim.initial_state=ic
        self.chosenestim.timerange=self.t
        
        self.chosenestim.input_mes=eval("self."+self.used_measurements_combobox.currentText())

    
        newgains=[]
        for i in range(len(self.gainsfieldslist)):
            if self.gainsfieldslist[i].text()!="NA":
                newgains.append(eval(self.gainsfieldslist[i].text()))
        
        self.chosenestim.gains=newgains
        self.chosenestim.run()
        self.currentoutput=self.chosenestim.output
        
        
    def wrapper_plot_est_output(self):
        global fig
        data=self.currentoutput
        plot_estim(data,self.t)
        show()
        draw()
        return
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

