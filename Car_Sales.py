#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
cs = pd.read_csv("C:\\Users\\umran\\Downloads\\Car_sales.csv")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


cs


# In[3]:


cs.fillna(0)


# In[4]:


cs.describe()


# In[ ]:





# In[6]:


cs["Manufacturer"].unique()


# In[9]:


cs.plot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


cs.isnull().sum()


# In[9]:


cs["Sales_in_thousands"].fillna(cs["Sales_in_thousands"].median(), inplace= True)

cs["Price_in_thousands"].fillna(cs["Price_in_thousands"].median(), inplace= True)
cs["Engine_size"].fillna(cs["Engine_size"].median(), inplace= True)
cs["Horsepower"].fillna(cs["Horsepower"].median(), inplace= True)
cs["Wheelbase"].fillna(cs["Wheelbase"].median(), inplace= True)
cs["Width"].fillna(cs["Width"].median(), inplace= True)
cs["Length"].fillna(cs["Length"].median(), inplace= True)
cs["Curb_weight"].fillna(cs["Curb_weight"].median(), inplace= True)
cs["Fuel_capacity"].fillna(cs["Fuel_capacity"].median(), inplace= True)                   
cs["__year_resale_value"].fillna(cs["__year_resale_value"].median(), inplace = True)
cs["Power_perf_factor"].fillna(cs["Power_perf_factor"].median(), inplace= True)


# In[10]:


cs


# In[21]:


cs.columns.tolist()


# In[20]:


sns.boxplot(cs["Price_in_thousands"])
plt.title("Price In Thousands ", size = 15)
plt.show()


# In[26]:


def remove_outliers(col):
    sorted(col)
    Q1,Q2 = col.quantile([0.25,0.75])
    IQR = Q2 - Q1
    lower_range = Q1 - (1.5*IQR)
    upper_range = Q2 + (1.5*IQR)
    return lower_range , upper_range


# In[28]:


lowerprice, upperprice = remove_outliers(cs["Price_in_thousands"])
cs["Price_in_thousands"] = np.where(cs["Price_in_thousands"]>upperprice, upperprice, cs["Price_in_thousands"])
cs["Price_in_thousands"] = np.where(cs["Price_in_thousands"]<lowerprice, lowerprice, cs["Price_in_thousands"])


# In[29]:


sns.boxplot(cs["Price_in_thousands"])
plt.title("Price In Thousands without Outliers ", size = 15)
plt.show()


# In[30]:


sns.scatterplot(x = "Horsepower", y = "Sales_in_thousands", data=cs)
plt.title("Correlation" , size = 15)
plt.show


# In[31]:


sns.scatterplot(x = "Engine_size", y = "Sales_in_thousands", data=cs)
plt.title("Correlation" , size = 15)
plt.show


# In[33]:


price = cs["Price_in_thousands"]*1000
sns.distplot(price, color="r")
plt.title("Density of Car Prices", size=15)
plt.xlabel("Price", size=13)
plt.ylabel("Density",size=13)
plt.show()


# In[35]:


plt.figure(figsize=(15,10))
sns.heatmap(cs.corr(), annot=True, square=True, cmap="RdBu")
plt.title("Correlation Between Variables", size=18)
plt.xticks(size=10)
plt.yticks(size=10)
plt.show()


# In[ ]:




