#!/usr/bin/env python
# coding: utf-8

# # Tiatanic Dateset
# ## Step 1: Data preprocessing & cleaning in Titanic Dataset

# In this notebook the very basic steps are been covered.This basic step can be applyed to any data visualzation and ML method.

# In[29]:


# Basic Python package!!!!!
import pandas as pd
import numpy as np 


# In[30]:


#Importing the required File
train_df =  pd.read_csv("train.csv")
test_df= pd.read_csv("test.csv")


# In[31]:


# To known what are the columns in your dataset
train_df.columns


# In[36]:


# Top 5 rows in your dataset 
train_df.head(10)


# In[33]:


#Bottom 5 rows in your dataset
train_df.tail()


# In[34]:


# Describe  function used to find the total count, mean, standard deviation, minimum value, maximum value,
#25,50,75 percentage of the dataset value
train_df.describe()


# In[14]:


#how many nulls
print(train_df.isnull().sum())


# In[37]:


# To remove the null values we can use fillna method 
# For example:
train_df.Cabin = train_df.Cabin.fillna("unknown")
print(train_df.isnull().sum())
# It is one of the method of data cleaning!!!!!!!!


# In[18]:


#how does the data looks like
print(train_df.shape)# total rows X column  count 
print("\n")
print(train_df.dtypes)# Each column data type


# In[24]:


# info gives count and datatype of it
train_df.info()
print('_'*40)
test_df.info()

