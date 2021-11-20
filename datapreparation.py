"""
Created on Tue Nov 16 18:57:28 2021
Es un programa para crear datasets de unidades de materia prima a granel
@author: lfigueroa
"""

import numpy as np
import pandas as pd


y=2020
n=10 #es el numero de unidades diarias a producir
mes=np.arange(1,366) #de 1 a (dias del mes + 1)
ouput=[]
for i in mes:
    datos=32+np.random.rand(n)+np.random.rand(n)
    df=pd.DataFrame(data=datos, columns=["net_weight"])
    df['day']=i # i es el dia del mes
    df['material']='sand'
    df['supplier']='SC' # colocar ds letras en mayusculas
    df['year']=y
    df['nro']=range(1,len(df)+1) #un numero de orden de produccion
    df['psd_mesh12']=1+2*np.random.rand(n)+1+2*np.random.rand(n)
    df['psd_mesh16']=6+3*np.random.rand(n)+3*np.random.rand(n)
    df['psd_mesh20']=10+3*np.random.rand(n)+2*np.random.rand(n)
    df['psd_mesh40']=10+3*np.random.rand(n)+3*np.random.rand(n)
    df['psd_mesh80']=22+3*np.random.rand(n)+3*np.random.rand(n)
    df['psd_mesh100']=13+3*np.random.rand(n)+3*np.random.rand(n)
    df['psd_mesh200']=2+2*np.random.rand(n)+np.random.rand(n)
    df['psd_meshPAN']=100-df['psd_mesh12']-df['psd_mesh16']-df['psd_mesh20']-df['psd_mesh40']-df['psd_mesh80']-df['psd_mesh100']-df['psd_mesh200']
    ouput.append(df)
ouput=pd.concat(ouput)
ouput.to_csv(str(y)+"_sandSC_.csv",sep=",")
