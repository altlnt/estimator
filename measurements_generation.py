# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:14:18 2017

@author: alex
"""

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import math
from pylab import *
from pykalman import UnscentedKalmanFilter
import time
import matplotlib.pyplot as plt

def gen_measurements(mainwind,data_combox_list,tacq=10,fech=1,acc_noise_max=20,gyro_noise=3,mag_noise_max=0.3,acc_bias=0,gyro_bias=3,g=9.81,real_m=array([2.19,1.82,3.31])):
    
    global t,measurements_corrupted,measurements_filtered,measurements_pure
    print('Begginning...')    
    date=time.strftime("%H:%M:%S")
    #plt.close('all')
    
   
    
    ########
    t_acquisition=tacq#s
    print("t_acquisition= ",t_acquisition ," s")
    fech=10. #Hz
    print('fech = ', fech)
    mainwind.t=arange(0,t_acquisition,float(1/fech)) #4 min
        
    #########
    print('Pure measurements generating...')
    
    gyro_drift_variation_speed=5
    
    
    
    
    
    # Sensors data "pure"
    acc_m=-g*array([zeros(int(t_acquisition*fech)) \
                 ,zeros(int(t_acquisition*fech)) \
                 ,ones(int(t_acquisition*fech))])
                 
    gyro_m=0*array(acc_m)
    a,b,c=real_m[0],real_m[1],real_m[2]
    mag_m=array([a*ones(int(t_acquisition*fech)) \
                 ,b*ones(int(t_acquisition*fech)) \
                 ,c*ones(int(t_acquisition*fech))])
    
    mainwind.measurements_pure={'acc':acc_m,'gyro':gyro_m,'mag':mag_m}
    print('Pure measurements generated...')
    measurements_pure=mainwind.measurements_pure
    
    # Sensors data "ccorrupted"
    print('Corrupted measurements generating...')
    
    acc_noise=acc_noise_max*random(acc_m.shape)
    acc_noise-=mean(acc_noise)
    acc_m_corr=acc_m+acc_noise
    
    
    gyro_m_corr=0*array(acc_m)+(gyro_noise*(random(acc_m.shape)-0.5))
    
    drift=gyro_drift_variation_speed*array([random(1),\
                       random(1),\
                       random(1)])
                       
    gyro_m_corr+=drift
    
    
    mag_noise=mag_noise_max*random(mag_m.shape)
    mag_noise-=mean(mag_noise)
    mag_m_corr=array([a*ones(int(t_acquisition*fech)) \
                 ,b*ones(int(t_acquisition*fech)) \
                 ,c*ones(int(t_acquisition*fech))])+mag_noise
    
    
    
    mainwind.measurements_corrupted={'acc':acc_m_corr,'gyro':gyro_m_corr,'mag':mag_m_corr}
    print('Corrupted measurements generated...')
    measurements_corrupted=mainwind.measurements_corrupted
    ##############                  FILTER PART
    ##############
    print('Filtering Corrupted measurements...')
    
    ###             FILTERING ACCELERATION
    Q=0.01*eye(3)
    R=10*eye(3)
    
    def fukf(state,noise):
        return state+noise
    
    ukf=UnscentedKalmanFilter(fukf,fukf,transition_covariance=Q,observation_covariance=R)
    acc_f=ukf.filter(measurements_corrupted['acc'].T)[0].T
    
    ###             FILTERING MAGNETOMETER
    
    Q=0.01*eye(3)
    R=10*eye(3)
    
    def fukf(state,noise):
        return state+noise
    
    ukf=UnscentedKalmanFilter(fukf,fukf,transition_covariance=Q,observation_covariance=R)
    mag_f=ukf.filter(measurements_corrupted['mag'].T)[0].T
    
    ###             FILTERING GYRO
    
    Q=0.01*eye(3)
    R=10*eye(3)
    
    def fukf(state,noise):
        return state+noise
    
    ukf=UnscentedKalmanFilter(fukf,fukf,transition_covariance=Q,observation_covariance=R)
    gyro_f=ukf.filter(measurements_corrupted['gyro'].T)[0].T
    
    mainwind.measurements_filtered={'acc':acc_f,'gyro':gyro_f,'mag':mag_f}
    
    print('Filtered Corrupted measurements generated...')
    
    for data_combox in data_combox_list:
        data_combox.addItem("measurements_filtered")
        data_combox.addItem("measurements_corrupted")
        data_combox.addItem("measurements_pure")
    
    
def plot_to_graphic(data,t):
    global fig
    
    fig=plt.figure()
    a=fig.add_subplot(311)
    m=fig.add_subplot(312)
    gy=fig.add_subplot(313)
    plt.ion()
    a.cla()
    m.cla()
    gy.cla()
    for n in range(3):
        a.plot(t,data['acc'][n],label=str(n+1))
        gy.plot(t,data['gyro'][n],label=str(n+1))
        m.plot(t,data['mag'][n],label=str(n+1))
        plt.legend()
        plt.draw()
        plt.legend()
    
    
    a.set_title('Accelero mes')
    m.set_title('Mag. mes')
    gy.set_title('Gyro mes')
    plt.legend()
    plt.title()
    fig.show()
    plt.draw()
    return 
    
def plot_estim(data,t):
    global Fig
    Fig=plt.figure()
    
    #So that figure adds the right number of subplots
    nchannels=min(data.shape)
    nsp=int(nchannels)
    while nsp%sqrt(nsp)!=0 and round(sqrt(nsp))!=sqrt(nsp):
        nsp+=1
             
    for i in range(nchannels):
        a=Fig.add_subplot(sqrt(nsp),sqrt(nsp),1+i) #i starts at 0
        a.plot(t,data[:,i].T,label='esti'+str(i))
        a.legend()
    Fig.canvas.set_window_title('Estimated plot')

        