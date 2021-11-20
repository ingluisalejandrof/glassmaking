"""
Created on Wed Nov 17 17:21:05 2021
Para evaluar la calidad de la produccion
@author: lfigueroa
"""

import pandas as pd
# Tres anos de produccion
df1=pd.read_csv('2018_sandSC_.csv')
df2=pd.read_csv('2019_sandSC_.csv')
df3=pd.read_csv('2020_sandSC_.csv')

#Flags por altos porcentajes (flg_WH  )
df1['flg_WH12'] = df1['psd_mesh12'].apply(lambda x: 1 if x>=5 else 0)
df1['flg_WH16'] = df1['psd_mesh16'].apply(lambda x: 1 if x>=10 else 0)
df1['flg_WH20'] = df1['psd_mesh20'].apply(lambda x: 1 if x>=13 else 0)
df1['flg_WPAN'] = df1['psd_meshPAN'].apply(lambda x: 1 if x>=21 else 0)

#Flags por bajos porcentajes (flg_WL  )
df1['flg_WL20'] = df1['psd_mesh20'].apply(lambda x: 1 if x<11 else 0)
df1['flg_WL40'] = df1['psd_mesh40'].apply(lambda x: 1 if x<11 else 0)
df1['flg_WL80'] = df1['psd_mesh80'].apply(lambda x: 1 if x<23 else 0)
df1['flg_WL100'] = df1['psd_mesh100'].apply(lambda x: 1 if x<10 else 0)


df1.to_csv("analisis_sand_2018.csv",sep=",")
