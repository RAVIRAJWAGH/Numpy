#!/usr/bin/env python
# coding: utf-8

# # Numpy and lambda function
# june batch

# In[1]:


import numpy as np


# In[4]:


arr=np.array([1,2,3,4,5,2,6])
arr


# In[5]:


np.where(arr==2)


# In[8]:


arr=np.array([1,2,3,4,5,2,4,6])
arr


# In[10]:


arr.reshape(4,2)


# In[11]:


np.sort(arr)


# In[12]:


arr[arr>2]


# In[13]:


arr>2


# In[15]:


# or
arr[[False, False,  True,  True,  True, False,  True,  True]]


# In[16]:


# join


# In[20]:


arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])


# In[24]:


np.concatenate((arr1,arr2))


# In[33]:


arr3=np.array([1,2,3,4,5,6])
arr3


# In[35]:


np.split(arr3,2) #array should be compatible


# In[36]:


# Lambda function


# In[43]:


def SQUARE(x):
    sq=x**2
    return sq


# In[44]:


SQUARE(4)


# In[38]:


square=lambda x:x**2


# In[45]:


square(5)


# In[51]:


li=[1,2,3,4,5]


# In[56]:


new_list=list(map(lambda x:x**3,li))
new_list


# In[52]:


map(square,li)


# In[57]:


list(map(lambda x:x*x, li)) #map


# In[60]:


list(filter(lambda x:x<4, li)) #filter


# In[ ]:




