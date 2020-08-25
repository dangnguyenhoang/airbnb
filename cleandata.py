import pandas as pd
import csv

# class cleandata:
#     def __init__(self,path):
#         self.path=path
def dataclean(path):
    #EDIT/ADD COLUMNS TO AIRBNB DATASET (df)
    #add activity column
    #activity = No Record if no last review
    #activity = Inactive if last review is not within 1year of the latest last_review
    #activity = Active otherwise
    #convert to datetime
    df= pd.read_csv(path)
    df['last_review'] = pd.to_datetime(df['last_review'])
    time_threshold = pd.to_datetime('2018/12/06')
    df.loc[df['last_review'] >= time_threshold, 'activity'] = 'Active'
    df.loc[df['last_review'] < time_threshold, 'activity'] = 'Inactive'
    df.loc[df['last_review'].isnull(), 'activity'] = 'No Record'
    df_active = df.loc[df['activity'] == 'Active']
    df_active
    df_active['occupancy_%'] = round(100 - df_active['availability_365']/ 365 * 100).astype('float')
    df_active.reset_index(inplace=True)
    df_active.drop(['index'], axis=1, inplace=True)
    return df
