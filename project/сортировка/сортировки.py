#!/usr/bin/env python
# coding: utf-8

# In[139]:


import random
from datetime import datetime


# BUB1. +1 байт. Реализовать алгоритм BubbleSort.

# In[6]:


def BubbleSort(mas):
    for i in range(len(mas)-1):
        for j in range(len(mas)-1):
            if mas[j]>mas[j+1]:
                element = mas[j+1]
                mas[j+1]=mas[j]
                mas[j]=element
    return mas


# BUB2. +1 байт. Оптимизировать алгоритм BubbleSort.

# In[16]:


def BubbleSortShift(mas):
    swap = True
    while swap==True:
        swap=False
        for i in range(len(mas)-1):
            if mas[i]>mas[i+1]:
                swap = True
                element = mas[i+1]
                mas[i+1]=mas[i]
                mas[i]=element            
    return mas            


# INS1. +1 байт. Реализовать алгоритм InsertionSort.

# In[38]:


def InsertionSort(mas):
    for i in range(1,len(mas)):
        element = mas[i]
        j = i - 1
        while j>=0 and mas[j]>element:
            mas[j+1]=mas[j]
            j-=1
        mas[j + 1]=element
    return mas    


# INS3. +1 байт. Оптимизировать алгоритм InsertionSort, сделать бинарный поиск места вставки.

# In[55]:


def bin_search(mas,i):
    first=0
    last=len(mas)-1
    mid=(first+last)//2
    while first<=last:
        if i>mas[mid]:
            first=mid+1
        if i<mas[mid]:
            last=mid-1
        if i==mas[mid]:
            return mid
        mid=(first+last)//2
    return first 


# In[111]:


def InsertionSortShift(mas):
    for i in range(1, len(mas)):
        kl = mas[i]
        ll = bin_search(mas[:i], kl)
        for k in range(i, ll, -1):
            mas[k] = mas[k - 1]
        mas[ll] = kl
    return mas    


# SHS1. +1 байт. Реализовать алгоритм ShellSort.

# In[64]:


def ShellSort(mas):
    b=len(mas)
    k=b//2
    while k>0:
        for i in range(0,b-k):
            j=i
            while (j>=0) and (mas[j]>mas[j+k]):
                element=mas[j]
                mas[j]=mas[j+k]
                mas[j+k]=element
                j-=1
        k=k//2
    return mas    


# In[150]:


massive = [92, 60, 80, 64, 43, 61, 57, 76, 62, 13, 80, 49, 0, 83, 17]


# In[143]:


BubbleSort(massive)


# In[145]:


BubbleSortShift(massive)


# In[147]:


InsertionSort(massive)


# In[149]:


InsertionSortShift(massive)


# In[151]:


ShellSort(massive)


# +2 байта. Занести в сравнительную таблицу время сортировки случайного массива размером 100, 1000 и 10000 для каждого алгоритма.

# In[137]:


massive = []
for i in range(10**4):
    massive.append(random.randint(0,10**4))


# In[128]:


t1 = datetime.now()
BubbleSort(massive)
print(datetime.now()-t1)


# In[130]:


t1 = datetime.now()
BubbleSortShift(massive)
print(datetime.now()-t1)


# In[132]:


t1 = datetime.now()
InsertionSort(massive)
print(datetime.now()-t1)


# In[138]:


t1 = datetime.now()
InsertionSortShift(massive)
print(datetime.now()-t1)


# In[136]:


t1 = datetime.now()
ShellSort(massive)
print(datetime.now()-t1)

