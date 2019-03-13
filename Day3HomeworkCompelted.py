#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


path = 'https://raw.githubusercontent.com/vikrambj2019/basic/master/Data/'
filename_read=os.path.join(path,'boston-house-prices.csv')
df=pd.read_csv(filename_read,na_values=['NA','?'])


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df[:3]


# In[7]:


df[23:27]


# In[8]:


df.describe()


# In[9]:


df.mean()


# In[11]:


round(df['AGE'].mean(),2)


# In[13]:


round(df['AGE'].describe(),2)


# In[14]:


df.info


# In[15]:


df.dtypes


# In[16]:


df.columns


# In[19]:


len(df)


# In[20]:


df['AGE'].value_counts()


# In[21]:


df.head()


# In[22]:


df['taxperrm']=df['TAX']/df['RM']


# In[23]:


df['taxperrm'].head()


# In[24]:


df.head()


# In[25]:


df['taxbyage']=df['TAX']/df['AGE']


# In[26]:


df.head()


# In[27]:


df.tail()


# In[28]:


df[df['TAX'].isnull()]


# In[29]:


for i in df.columns:
   print(df[df[i].isnull()]) 


# In[31]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib','inline')
df['TAX'].plot()


# In[32]:


import random


# In[33]:


df['rand_val']=random.randint(1,10)
#bad way to do it because it needs to loop through or else every cell 
#is the same number and not different like we need


# In[34]:


df.head()


# In[35]:


df.tail()


# In[37]:


for i in range(len(df)):
    df.iloc[i:-1]=random.randint(1,10)


# In[38]:


df.head(10)


# In[39]:


df['rand_val'].value_counts()


# In[40]:


df['rand_val'].unique()


# In[42]:


import numpy as np


# In[44]:


df.pivot_table(index=['AGE','TAX'],values=['RM'],aggfunc=np.mean)


# In[48]:


df[df['TAX']>15].count()


# In[49]:


df['TAX']>15


# In[62]:


df_70 = df[df['rand_val']<8]


# In[60]:


df_70['AGE'].value_counts()


# In[63]:


df_70.head()


# In[65]:


df_70['rand_val'].unique()


# In[72]:


df_20 = df[df['rand_val']==8]


# In[74]:


df_20 = df_20.append(df[df['rand_val']==9])


# In[75]:


df_20['rand_val'].unique()


# In[76]:


df_10 = df[df['rand_val']==10]


# In[77]:


df_10['rand_val'].unique()


# In[79]:


print(len(df_70))
print(len(df_20))
print(len(df_10))


# In[80]:


print(len(df_70)+len(df_20)+len(df_10))


# In[81]:


len(df)


# In[83]:


path = 'https://raw.githubusercontent.com/vikrambj2019/basic/master/Data/'
filename_read=os.path.join(path,'boston-house-prices_metadata.txt')
dftxt=pd.read_fwf(filename_read,na_values=['NA','?'])


# In[84]:


dftxt.head()


# In[85]:


path = 'https://raw.githubusercontent.com/vikrambj2019/basic/master/Data/'
filename_read=os.path.join(path,'boston-house-prices_metadata.txt')
dftxt=pd.read_csv(filename_read,delimiter="\t")


# In[86]:


dftxt.head()


# In[ ]:




