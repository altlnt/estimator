# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:25:22 2017

@author: alex
"""
from pykalman import UnscentedKalmanFilter

from pylab import *
class estimator():
    def __init__(self):
        self.name="UKF bitches"
        #Computing attributes
        
        "Fonction f'(x)"
        self.costf=None
        self.output=array([])
        self.gains=[1.1,1.2]
        self.timerange=array([])
        
        
        #GUI attributes
        self.description='A UKF filter, using PyKalman.'
        self.description=self.description+' Measurements are [3,len(t)]'
        self.description+='They must be converted to [len(t),3].T'
        "Description of the estimator"
        
        self.input_mes=array([])
        "Used inputs (filtered, corrupted, pure..)"        
        
        
        self.gains_name=['Q','R']
        "Name of the gains"        
        
        self.output=array([])
        "Output of the estimator"        
              
        self.initial_state=zeros(self.output.shape)
        "Self Explainatory"
        
    def run(self):
        "Main run function for the estimator"
        print('Defining transition func')
        def f(state,noise):
            return state+noise
        Q=eye(3)*self.gains[0]
        R=eye(3)*self.gains[1]
        print('Defining the ukf...')
        ukf=UnscentedKalmanFilter(f,f,Q,R,initial_state_mean=zeros(min(self.input_mes['acc'].shape)))
        
        print('Filtering')
        self.output=ukf.filter(self.input_mes['acc'].T)[0]
        print('Done')
        return
        


def def_estim():
    print("Setting up estimator..")
    e=estimator()
    print("Done")
    #Pimp the estimator as you like

    return e
