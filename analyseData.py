# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from glob import glob
import ntpath

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

def plotSoundData(df,colors,fileName,x='time',xlabel='Time in seconds'):
    f = plt.figure()
    df.plot(x=x,y='currSound',ax=f.gca(),color=colors)
    plt.legend().remove()
    plt.ylabel('Sound Intensity',fontsize=13,fontweight='bold')
    plt.xlabel(xlabel,fontsize=13,fontweight='bold')
    plt.tick_params(axis='both',which='major',labelsize=13)
    
    figName = '-'.join(fileName[:-4].rsplit('/',1)) + '.pdf'
    
    f.savefig(figName,bbox_inches='tight')
    

def importExperimentData(fileName,header):
    df = pd.read_csv(fileName,header=None,names=header)
    return df


if __name__ == '__main__':
    nestHeader = ['time','x','y','yaw']
    robotHeader = ['time','x','y','yaw','prevSound','currSound','turnProb','action']
    fileName = '../2019-09-19-0p5-log-rate/07-57-21-move-15m/robot1.csv'
    df = importExperimentData(fileName,header=robotHeader)
    colors = plt.cm.inferno(np.linspace(0,0.9,df[['x','currSound']].shape[1] - 1))
    
    plotSoundData(df,colors,fileName,x='x',xlabel='Distance in metres')
    
    
    