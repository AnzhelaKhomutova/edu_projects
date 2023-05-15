#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[[0,1,0,0,0,0,0,0],
   [0,0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0,0],
   [1,1,0,0,1,1,0,0],
   [0,0,0,0,0,0,1,0],
   [0,0,0,0,0,0,0,1],
   [0,0,0,0,0,0,0,1],
   [0,0,0,0,0,0,0,0]]


# In[2]:


b = [0]*len(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        b[j]+=a[i][j]


# In[3]:


c=[0]*len(a)


# In[4]:


dict_final={}


# In[5]:


level = 1

while 0 in b:
    dict_final[level]=[]
    for i,element in enumerate(b):       
        if element==0:
            print(f'level ={level}')  
            b[i]=-1
            for j in range(len(b)):
                c[j]=b[j]-a[i][j]  
                
            print(i)
            print(c)
            dict_final[level]+=[i]
            b = c.copy()
    level+=1


# In[6]:


dict_final

