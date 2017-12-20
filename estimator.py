# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:25:22 2017

@author: alex
"""
from pylab import *
class estimator():
    def __init__(self):
        self.name="name"
        #Computing attributes
        self.func=None 
        "Fonction f'(x)"
        self.costf=None
        self.output=array([])
        self.gains=[1.1,1.2,1.3]
        self.timerange=array([])
        
        
        #GUI attributes
        self.description='This_is_a_description'
        "Description of the estimator"
        
        self.input_mes=array([])
        "Used inputs (filtered, corrupted, pure..)"        
        
        
        self.gains_name=['Gain0','Gain1','Gain2']
        "Name of the gains"        
        
        self.output=array([])
        "Output of the estimator"        
              
        self.initial_state=zeros(self.output.shape)
        "Self Explainatory"
        
    def run(self):
        "Main run function for the estimator"
        a=1
        print('run')
        return 



def def_estim():
    e=estimator()
    #Pimp the estimator as you like

    return e

    