#!/usr/bin/env python
# coding: utf-8

# ###  +1 байт. Реализовать итеративный O(N) алгоритм возведения числа в степень.

# In[ ]:


p=1 #начальная позиция
d=1.001 #число для возведения в степень
n=1000 #степень


# In[4]:


new_d = 1
for i in range(n):
    new_d *= d


# In[5]:


new_d


# ### +1 байт. Реализовать рекурсивный O(2^N) и итеративный O(N) алгоритмы поиска чисел Фибоначчи.

# In[47]:


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# In[52]:


[fibonacci(i) for i in range(1,23,1)]


# In[9]:


f1=1
f2=1
a=[1,1]
for i in range(20):
    f=f1+f2
    f1=f2
    f2=f
    a.append(f)
print(a)   


# ### +1 байт. Реализовать алгоритм поиска количества простых чисел через перебор делителей, O(N^2).

# In[ ]:


#перебор делителей от 2 до квадратного корня из числа


# In[95]:


a=[]


# In[96]:


for i in range(1,31):
    sqrt = int(i**0.5)
    s=0
    for j in range(2,sqrt):
        if i%j==0 and i!=j:
            s+=1
    if s==0:
        a.append(i)


# In[97]:


a


# ### +1 байт. Реализовать алгоритм возведения в степень через двоичное разложение показателя степени O(2LogN) = O(LogN).

# In[15]:


p=1 #начальная позиция
d=1.001 #число для возведения в степень
n=1000 #степень


# In[35]:


p=1 #начальная позиция
d=2 #число для возведения в степень
n=5 #степень


# In[36]:


if n==0:
    p=1
    
while n>0 :
    if n % 2==0:
        n=n//2
        d=d*d
    else:
        n=n-1
        p=p*d


# In[37]:


p


# ### +1 байт. Реализовать алгоритм поиска чисел Фибоначчи по формуле золотого сечения.

# In[81]:


s = 1.618
a = [1,1]


# In[82]:


number = 1
for i in range(1,21):
    number = np.round(number*s,0)
    a.append(int(number))
print(a)


# ### +1 байт. Реализовать алгоритм "Решето Эратосфена" для быстрого поиска простых чисел O(N Log Log N).

# In[43]:


b=[]
for i in range(1,31):
    b.append(i)


# In[44]:


for i in range(2,len(b)):
    for j in range(len(b)):
        if b[j]%i==0 and b[j]!=i:
            b[j]=0
print(b)            


# In[46]:


[i for i in b if i>0]

