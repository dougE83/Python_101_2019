#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[103]:


path ='https://raw.githubusercontent.com/vikrambj2019/basic/master/Data/'
filename_read=os.path.join(path,'auto-mpg.csv')
df=pd.read_csv(filename_read,na_values=['NA','?'])
#create 4 files in starting, test, data, production, output folder#


# In[104]:


print(df)


# In[105]:


df.head(10)


# In[106]:


df.tail(10)


# In[107]:


df[:3]


# In[108]:


df[:5]


# In[109]:


df[10:17]


# In[110]:


df.describe()


# In[111]:


df.mean()


# In[112]:


round(df['mpg'].mean(),2)


# In[113]:


round(df['mpg'].describe(),2)


# In[114]:


df.info()


# In[115]:


df.dtypes


# In[116]:


columns_need=['mpg','cylinders','displacement']
df[columns_need].mean()


# In[117]:


df.columns


# In[118]:


df.columns


# In[119]:


len(df)


# In[120]:


df['mpg'].value_counts()


# In[121]:


df.shape


# In[122]:


df['wtpercyl']=df['weight']/df['cylinders']


# In[123]:


df.head()


# In[124]:


df['dispercyl']=df['displacement']/df['cylinders']


# In[125]:


df.head()


# In[126]:


df[df['horsepower'].isnull()]


# In[127]:


for i in df.columns:
    #print(i)
    print(df[df[i].isnull()])


# # load data, print head, check for columns, check for nulls then deciede on what to do if you do or don't.

# In[85]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df['mpg'].plot()


# In[136]:


# I want to break my datafile into 3 parts (equal), randomly.
# I need a panads file
# df['rand_val']
import random
df['rand_val']=random.randint(1,3)


# In[93]:


df.head()


# In[138]:


for i in range(len(df)):
    df.iloc[i:,-1]=random.randint(1,3)


# In[140]:


df.head(20)


# In[152]:


df.iloc[0,11]


# In[153]:


for i in range(len(df)):
    df.iloc[i,11]=random.randint(1,3)


# In[154]:


df.head()


# In[155]:


df['rand_val'].value_counts()


# In[160]:


df['rand_val'].unique()


# In[169]:


import numpy as np
df.pivot_table(index=['cylinders','origin'],values=['mpg'],aggfunc=np.mean)#len to get a count


# In[172]:


df[df['mpg']<15].count()


# In[181]:


#df[df['mpg']<15]


# In[177]:


df_1 = df[df['rand_val']==1]
df_2 = df[df['rand_val']==2]
df_3 = df[df['rand_val']==3]


# In[180]:


print(len(df_1))
print(len(df_2))
print(len(df_3))


# In[182]:


#trying to creat a loop to create the subset tables from above
# for i in
df['rand_val'].unique()


# In[185]:


df_1 = df_1.append(df_2)


# In[186]:


df_1 = df_1.append(df_3)


# In[187]:


len(df_1)


# In[ ]:


# Homework for class 4: 
# Do all(most) of what we did with the new dataset, divide the data into 70/20/10 split
# Find the funtion to read, text, and Excel

