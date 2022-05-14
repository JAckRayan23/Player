import pandas as pd
import numpy as np
df=pd.read_csv('C:\\Users\\Vicky\\OneDrive\\Desktop\pseudo_facebook.csv')
print(df)
print(df.drop('dob_day',1))
print(df.shape)
d_f=df[2:10][1:5]
print(df)
df1 = pd.DataFrame({'employe':['Bob','lake','Lisa'],'group':['account','Engineering','HR']})
df2 = pd.DataFrame({'employe':['Bob','lake','Lisa'],'hire_date':['2004','2006','2004']})
print(df1,df2)
df3=pd.merge(df1,df2)
print(df3)
df3.sort_values(by=['hire_date'])
print(df3)
print(pd.wide_to_long)
print(df.transpose())
print(df.shape)
a1=np.arange(10)
print('Array 1 \n', a1)
a3=np.arange(10).reshape(5,2)
print('array 3 with 5 rows and 2 columns \n', a3)
df.isnull().sum()
d_f=df[['age','dob_day','dob_year']]
print(d_f.head(11))
print(df)

