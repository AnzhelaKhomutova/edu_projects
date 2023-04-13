#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np
import os


# In[165]:


def factorial(x):
    if x==0:
        return 1
    if x==1:
        return x
    if x>1:
        return x*factorial(x-1)


# In[166]:


def func(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))


# In[184]:


def calc(nn):
    s=0
    n=2*nn
    N_=(n//2)*9
    m=10
    r=int((N_/m))
    for i in range(r+1):
        s+=((-1)**i)*func(n,i)*func((n+N_-i*m-1),(n-1))
    return round(s) 


# In[5]:


nn=1 #поступает из файла


# In[169]:


mypath=r'D:\MyDesktop\сч билеты\test'


# In[187]:


for file in os.listdir(mypath):
    f = os.path.join(mypath,file)
    if ('.in' in file) and ('.out' not in file):
        par_in_f = open(f)
        par_in = par_in_f.read()
        #calc(int(par_in))
        for file2 in os.listdir(mypath):
            f2 = os.path.join(mypath,file2)    
            if ('.out' in file2 and '.in' not in file2) and (file[:6]==file2[:6]):
                #print(file2)
                par_out_f = open(f2)
                par_out = par_out_f.read()
                print("n="+str(par_in))
                print ("Мой результат =" + str(calc(float(par_in))))
                print("Результат выходного файла = "+str((par_out)))
                print("Разница ="+str(float(calc(float(par_in)))-(float(par_out))))
                if float(calc(float(par_in)))==(float(par_out)) :
                    print('верно')
                else:
                    print('неверно')
                print('')   

