# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:55:43 2017

@author: alex
"""
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
        data=eval("self.cdata")
        plot_to_graphic(data)
        show()
        draw()
        return
        
        
        
        
        
    def connect_estim_tab(self):
        self.chosenestim=None
        self.estim_list=[]
        
        self.gainslabellist=[eval("self.label_Gain"+str(i)) for i in range(6)]
        
        self.gainsfieldslist=[eval("self.edit_gain"+str(i)) for i in range(6)]
        
        self.import_estimator_button.clicked.connect(self.wrapper_import_estimator)
        self.estim_selec_button.clicked.connect(self.wrapper_select_estimator)
        
    def wrapper_import_estimator(self):
        p=QtGui.QFileDialog.getOpenFileNames()[0]
        
        #Car sinon il y a un u devant, no comprende porqe
        foo = imp.load_source('estimator', p)
        self.estim_list.append(foo.def_estim())
        self.estimators_combobox.addItem(self.estim_list[-1].name)
    
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
        

        
        