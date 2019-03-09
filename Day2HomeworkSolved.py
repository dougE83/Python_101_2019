# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:40:34 2019

@author: Doug's Surface

10 math funtions
addition-
subtraction-
division-
multiplication-
sqrt
exponet
sin-
cos-
tan-
log-
"""

import numpy as np

a = 2
b = 3

c=a+b
d=a-b
e=a/b
f=a*b
g=np.sin(np.array((a,b)))
j=np.sin(a)
h=np.cos(np.array((a,b)))
k=np.cos(a)
i=np.tan(np.array((a,b)))
l=np.tan(a)
m=a**b
n=np.sqrt(a)
o=np.power(a,b)

print(c,d,e,f,g,h,i,j,k,l,m,n,o)

#printing prime numbers only
for num in range(1,101 + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

#printing even numbers only
for num in range(1,101):
    if num % 2 == 0:
        print(num)
    
#printing odd numbers only
for num in range(1,101):
    if num % 2 > 0:
        print(num)
        
        
#FizzBuzz Solution
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
        
        











            