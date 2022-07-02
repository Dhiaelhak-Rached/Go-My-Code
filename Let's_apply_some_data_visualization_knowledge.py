#!/usr/bin/env python
# coding: utf-8

# In[83]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('titanic-passengers.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.isnull().sum().sum()


# In[8]:


df.drop("Cabin",inplace=True,axis=1)


# In[9]:


df.head()


# In[10]:


df["Age"].fillna(df["Age"].median(), inplace = True)


# In[11]:


df.isnull().sum()


# In[12]:


df.dropna(inplace=True,axis=0)


# In[13]:


df.isnull().sum()


# In[14]:


plt.figure(figsize=(10,6))
plt.title("Ages ")
plt.xlabel("Age")

df["Age"].plot.hist()


# In[15]:


fig ,ax = plt.subplots(1,1,figsize=(6,6))
df['Survived'].value_counts().plot.pie(explode=[0,0.1],
                                          autopct='%1.1f%%',
                                          ax=ax,
                                          colors = ["red","pink"],
                                          center = (10,0),
                                          shadow=True)

ax.set_title('Percentage number of survived passengers')


# In[93]:


plt.figure(figsize=(10,6))
sns.barplot(x= 'Age', y = 'Survived', data = df)


# In[19]:


plt.figure(figsize=(10,6))
sns.barplot(x= 'Sex', y = 'Survived', data = df) 


# In[20]:


plt.figure(figsize=(10,6))
plt.title(" Ages ")
plt.xlabel("Age")

df["Age"].plot.hist()


# In[82]:


plt.figure(figsize=(10,6))
plt.title("Count ")
plt.xlabel("Embarked")
plt.ylabel("Count")
vc=df['Embarked'].value_counts()
vc.plot.bar(rot=0)


# In[83]:





# In[21]:


plt.figure(figsize=(10,6))
plt.title("Count ")
plt.xlabel("Parch")
plt.ylabel("Count")
vc=df['Parch'].value_counts()
vc.plot.bar(rot=0)


# In[24]:


s=sns.FacetGrid(df,col="Survived")
s.map(plt.hist,'Age',bins=20)
s=sns.FacetGrid(df,col="Sex")
s.map(plt.hist,'Age',bins=20)


# In[101]:


def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 0

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
plot_correlation_map( df )


# this function show a table which displays the correlation coefficients for different columns.

# In[13]:


df[["Pclass", "Survived"]].groupby(["Pclass"], as_index=True).mean()


# In[28]:


df.drop("Name",inplace=True,axis=1)


# In[14]:


df.head()


# In[14]:


Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer",

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty",

                  "the Countess": "Royalty",

                    "Dona":       "Royalty",

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs",

                    "Master" :    "Master"

                    }


# In[15]:



df[['First','Last']]=df.Name.str.split(', ',expand=True)

df.Last.head()


# In[16]:


df[['Title','av','df']]=df.Last.str.split('.',expand=True)
df.head()


# In[17]:


df['Title']=df['Title'].replace(Title_Dictionary)


# In[18]:


df.Title.value_counts()


# In[19]:


df.drop("av",inplace=True,axis=1)
df.drop("df",inplace=True,axis=1)
df.drop("Last",inplace=True,axis=1)


# In[20]:


df


# In[21]:


plt.figure(figsize = (10, 8))
sns.heatmap(df[["Age","Sex","Fare"]].corr(), annot = True)


# In[92]:


df['Title'].corr(df['Survived'])


# In[91]:





# In[97]:


df['FamilySize'] = df['SibSp'] + df['Parch'] + 1


# In[96]:


df


# In[99]:


plt.figure(figsize=(10,6))
sns.barplot(x= 'FamilySize', y = 'Survived', data = df) 


# In[ ]:




