#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# # Drop unnamed coloumn

# In[9]:


df = df.drop("Unnamed: 0", axis=1)
print(df.head())


# Gender Distribution

# In[32]:


plt.figure(figsize = (4,5))
ax = sns.countplot(data = df, x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Discription")
plt.show()


# In[ ]:


#From the above chart we have analysed that:
#The no.of females in the data is more than the no.of males


# In[20]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[31]:


plt.figure(figsize = (3,3))
sns.heatmap(gb, annot=True)
plt.title("Relationship Between Parents Education & Student Score")
plt.show()


# In[25]:


#From the above chat we have concluded that the education of the parent have a good impact on their student


# In[29]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)


# In[33]:


plt.figure(figsize = (3,3))
sns.heatmap(gb1, annot=True)
plt.title("Relationship Between Parents MaritalStatus & StudentScore")
plt.show()


# In[34]:


#from the above chart we have concluded that their is no impact on the
#student's score due to their parent's martial status


# In[35]:


sns.boxplot(data = df, x = "ReadingScore")
plt.show()


# In[37]:


sns.boxplot(data = df, x = "WritingScore")
plt.show()


# In[38]:


sns.boxplot(data = df, x = "MathScore")
plt.show()


# In[42]:


print(df["EthnicGroup"].unique())


# # Distrinution Of Ethenic Groups

# In[54]:


groupA = df.loc[(df['EthnicGroup']=="group A")].count()
groupB = df.loc[(df['EthnicGroup']=="group B")].count()
groupC = df.loc[(df['EthnicGroup']=="group C")].count()
groupD = df.loc[(df['EthnicGroup']=="group D")].count()
groupE = df.loc[(df['EthnicGroup']=="group E")].count()

l=["group A", "group B","group C", "group D", "group E"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]

plt.pie(mlist, labels = l, autopct = "%1.2f%%")
plt.title("Distribution Of Ethnic Groups")
plt.show()


# In[55]:


ax = sns.countplot(data = df, x = 'EthnicGroup')
ax.bar_label(ax.containers[0])


# # ThankYou

# In[ ]:




