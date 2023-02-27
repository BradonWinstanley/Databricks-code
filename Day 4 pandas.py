# Databricks notebook source
# DAY 4

import pandas as pd



# COMMAND ----------

#dict1 = {'key'  :  'value'}

df = pd.DataFrame({
    'a' :[1,2,3],
    'b' :[4,5,6],
    'c' :[7,8,9],
}, index = [1,2,3])

df2 = pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
      index=[1,2,3],
      columns = ['a', 'b', 'c']
     
print(df)
print("Break")
print(df2)
  

# COMMAND ----------

#df.loc [1,'c'] used to look up points on table (1,2)
#df.iloc [0,2]  used to look up actual point eg. 0,2 is actually 1,3

#pd.concat ([df,df], axis=1) used to transpose data

#df.sort=values ('a', ascending=False) used to sort data across
#df.sort-values (1, axis=1, ascending=False) used to sort data down

#df.drop(colums='c') deletes a column specified
#df.drop([1,3])

# COMMAND ----------

tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
#print (tipsData(5)) #prints top 5
#print (tipsData.describe()) #shows info quick

#print(tipsData.isnull().sum()) #shows data errors

# COMMAND ----------

tipsData.groupby(['day']).count() # consolidates datapoints

# COMMAND ----------

tipsData.groupby(['day']).sum() # creates a sum of data

# COMMAND ----------

totaltips = tipsData.groupby(['day']).sum()['tip'] #shows how many tips made in a day
totalbill = tipsData.groupby(['day']).sum()['total_bill']

tipdaypercentage = print(100*totaltips / totalbill)
tipdaypercentage = tipdaypercentage.to_frame('tip(%)').reset_idex() #shows average tips for each day

print(tipdaypercentage)

# COMMAND ----------


