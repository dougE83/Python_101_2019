#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import pandas as pd
import numpy as np


# In[2]:


def sudokuNineByNine(df):
    ls=df.values # Convert panadas to numpy array
    ls[np.isnan(ls)]=0 # Convert Nulls to zeros
    a=np.argwhere(ls==0) # Saving the address locations of all zeros in array called "a"
    for i in range(len(a)):
        b=a[i]
    # a holds the address of all my zeros

        row=b[0] # Will give me the row of the first zero address
        col=b[1] # Will give me the column of the first zero address
        #ls[row] # Will give me the array of the row
        #ls[:,col] # Will give me the array of the column

        if a[i][0] in (0,1,2):
            row_sq=0
        elif a[i][0] in (3,4,5):
            row_sq=1
        else:
            row_sq=2
        
        #print(row_sq)
        
        if a[i][1] in (0,1,2):
            col_sq=0
        elif a[i][1] in (3,4,5):
            col_sq=1
        else:
            col_sq=2

        ls[row_sq:row_sq+3,col_sq:col_sq+3].reshape(1,9).flatten() # changing from 2x2 to 1x4 and flatten it out

        c=np.append(ls[row].tolist(),[ls[:,col].tolist(),ls[row_sq:row_sq+3,col_sq:col_sq+3].reshape(1,9).flatten().tolist()])
        # Showing the unique values that are listed in all 3 arrays ^

        list1=[1,2,3,4,5,6,7,8,9,0] # This is setting the list of all the values that are possible outcomes
        d=set(list1).difference(c) 
        ls[row,col]=list(d)[0] # Fills in the value with the value that was missing from the set 2 in this case

    return ls


# In[ ]:




