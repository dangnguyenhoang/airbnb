import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import math
import geopandas as gpd
import csv
import geoplot as gplt
from datetime import datetime
from pylab import *
from shapely.ops import nearest_points
from cleandata import dataclean
import streamlit as st
pd.options.mode.chained_assignment = None
# df= pd.read_csv(r'/Users/nguyenthiminhhien/Documents/Weekly Projects/nyc_airbnb.csv')
path=r'/Users/nguyenthiminhhien/Documents/Weekly Projects/nyc_airbnb.csv'
data=dataclean(path)
data=pd.DataFrame(data.head(10))
# df_Brooklyn=data.loc[data['neighbourhood_group']=='Brooklyn']
# df_Manhattan=data.loc[data['neighbourhood_group']=='Manhattan']
# df_Queens=data.loc[data['neighbourhood_group']=='Queens']
# df_StatenIsland=data.loc[data['neighbourhood_group']=='Staten Island']
# df_Bronx=data.loc[data['neighbourhood_group']=='Bronx']
st.dataframe(data.price)

# fig=plt.figure()
# fig,ax=plt.subplots(figsize=(40,20))
# x_position=np.arange(3)
# width = 0.15
# labelsbar=['Entirehome/apt','Private Room','Shared Room']
# ax.bar(x_position,df_Brooklyn.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='g',label='Brooklyn')
# ax.bar(x_position+0.15,df_Manhattan.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='y',label='Manhattan')
# ax.bar(x_position+0.3,df_Queens.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='pink',label='Queens')
# ax.bar(x_position+0.45,df_StatenIsland.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='cyan',label='Statenn Island')
# ax.bar(x_position+0.6,df_Bronx.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='violet',label='Bronx')
# ax.set_xticks(x_position+0.3)
# ax.set_xticklabels(labelsbar)
# ax.set_title('Room Quantity comparison')
# ax.legend()
# st.pyplot()
# ax[0][0].set_title('Brooklyn\nTotal:%s'%df_Brooklyn[['room_type']].count().tolist()[0])
# ax[0][0].legend()
# ax[0][1].pie(df_Manhattan[['room_type']].groupby(df_Manhattan['room_type']).count(),labels=['Entire home/apt','Private room','Shared room'],textprops=dict(color="w"),autopct='%1.1f%%')
# ax[0][1].set_title('Manhattan\nTotal:%s'%df_Manhattan[['room_type']].count().tolist()[0])
# ax[0][1].legend()
# ax[0][2].pie(df_Queens[['room_type']].groupby(df_Queens['room_type']).count(),labels=['Entire home/apt','Private room','Shared room'],textprops=dict(color="w"),autopct='%1.1f%%')
# ax[0][2].set_title('Queens\nTotal:%s'%df_Queens[['room_type']].count().tolist()[0])
# ax[0][2].legend()
# ax[1][0].pie(df_StatenIsland[['room_type']].groupby(df_StatenIsland['room_type']).count(),labels=['Entire home/apt','Private room','Shared room'],textprops=dict(color="w"),autopct='%1.1f%%')
# ax[1][0].set_title('StatenIsland\nTotal:%s'%df_StatenIsland[['room_type']].count().tolist()[0])
# ax[1][0].legend()
# ax[1][1].pie(df_Bronx[['room_type']].groupby(df_Bronx['room_type']).count(),labels=['Entire home/apt','Private room','Shared room'],textprops=dict(color="w"),autopct='%1.1f%%')
# ax[1][1].set_title('Bronx\nTotal:%s'%df_Bronx[['room_type']].count().tolist()[0])
# ax[1][1].legend()
# labelsbar=['Entirehome/apt','Private Room','Shared Room']
# x_position=np.arange(3)
# width = 0.15
# ax[1][2].bar(x_position,df_Brooklyn.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='g',label='Brooklyn')
# ax[1][2].bar(x_position+0.15,df_Manhattan.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='y',label='Manhattan')
# ax[1][2].bar(x_position+0.3,df_Queens.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='pink',label='Queens')
# ax[1][2].bar(x_position+0.45,df_StatenIsland.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='cyan',label='Statenn Island')
# ax[1][2].bar(x_position+0.6,df_Bronx.groupby(['neighbourhood_group','room_type']).count().id.tolist(),width,color='violet',label='Bronx')
# ax[1][2].set_xticks(x_position+0.3)
# ax[1][2].set_xticklabels(labelsbar)
# ax[1][2].set_title('Room Quantity comparison')
# ax[1][2].legend()
# fig.suptitle('Room type analysis')
# plt.show()