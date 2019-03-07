#!/usr/bin/env python
# coding: utf-8

# In[12]:


my_name = "Doug Devine"
my_age = "36"
my_weight = 150
my_height = 170
my_hair_color = "brown"
my_eyes_color = "blue"


# In[20]:


my_kg = my_weight*0.453592
my_BMI = my_kg/((my_height/100)**2)


# In[21]:


print ("My name is",my_name,"and my age is",my_age)
print (f"My name is {my_name} and my age is {my_age}")
print (f"My BMI is {my_BMI}")


# In[24]:


print (f"I want to show my BMI in two decimal places {round(my_BMI,2)}")


# In[25]:


print("I am not happy, I want to square my BMI, how do I do that?")


# In[29]:


import math as mt


# In[30]:


mt.sqrt(my_BMI)


# In[31]:


my_BMI**0.5


# In[56]:


round(mt.sqrt(my_BMI),2)


# # Introduction to conditions
# ** If BMI < 25 then print "Not obese" else print "obese" 

# In[52]:


if my_BMI < 25:
    print ("Not obese")
else:
    print ("Obese")


# In[70]:



my_BMI = 24

if my_BMI < 18:
    print("Not Healthy")
elif my_BMI >= 18 and my_BMI < 25:
    print("Not obese")
else:
    print("Obese")


# In[71]:


# get a random number between 1-6 if odd print r 


# In[78]:


import random


# In[102]:


print(random.randint(1,6))


# In[148]:


if random.randint(1,6) % 2 == 0:
    print("Even")
else:
    print("Odd")


# In[147]:


x = random.randint(1,6)
if x%2==0:
    print(x,"is Even")
else:
    print(x,"is Odd")


# In[156]:


x = random.randint(1,6)
if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
elif x==5:
    print("Five")
else:
    print("Six")


# In[163]:


# printing all number below 10


# In[162]:


range(1,10)


# In[177]:


for i in range(1,10):
    if i % 2 == 0:
        print(i,"Even")
    else:
        print(i,"Odd")


# 1) I need a for statment to print 1 to 101
# 2) check the i is divisible by 3 (use %), if true then print fizz
# 3) check if i is divisible by 5 (use %), if true print buzz
# 

# In[187]:


for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# In[ ]:




