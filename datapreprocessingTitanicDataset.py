import pandas as pd
import numpy as np

df=pd.read_csv(r'S:\Data Science Prakash Senapati\AllDatasets\titanic.csv')
df.tail()

df.describe()

del df['Name']
df.head()

del df['Ticket']
df.head()

del df['Fare']
df.head()

del df['Cabin']
df.head()

def getNumber(str):
    if str=='male':
        return 1
    else:
        return 0
df["Gender"]=df["Sex"].apply(getNumber)
df.head()

del df["Sex"]
df.head()

df.isnull().sum()

meanS=df[df.Survived==1].Age.mean()
meanS

df['age']=np.where(pd.isnull(df.Age)&df["Survived"]==1,meanS,df["Age"])
df.head()

df.isnull().sum()

meanNS=df[df.Survived==0].Age.mean()
meanNS

df.age.fillna(meanNS,inplace=True)
df.head()

df.isnull().sum()

del df['Age']
df.head()

survivedQ=df[df.Embarked=='Q'][df.Survived==1].shape[0]
survivedC=df[df.Embarked=='C'][df.Survived==1].shape[0]
survivedS=df[df.Embarked=='S'][df.Survived==1].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

survivedQ=df[df.Embarked=='Q'][df.Survived==0].shape[0]
survivedC=df[df.Embarked=='C'][df.Survived==0].shape[0]
survivedS=df[df.Embarked=='S'][df.Survived==0].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

df.dropna(inplace=True)
df.head()

df.isnull().sum()

df.rename(columns={'age':'Age'},inplace=True)
df.head()

df.rename(columns={'Gender':'Sex'},inplace=True)
df.head()

def getEmb(str):
    if str=='S':
        return 1
    elif str=='Q':
        return 2
    else:
        return 3
df["Embark"]=df["Embarked"].apply(getEmb)
df.head()

del df['Embarked']
df.rename(columns={'Embark':'Embarked'},inplace=True)
df.head()

import matplotlib.pyplot as plt
from matplotlib import style

males = (df['Sex'] == 1).sum() 
females = (df['Sex'] == 0).sum()
print(males)
print(females)
p = [males, females]
plt.pie(p,
       labels = ['Male', 'Female'], 
       colors = ['Gold', 'Silver'],
       explode = (0.12, 0),  
       startangle = 0)
plt.axis('equal') 
plt.show()

MaleS=df[df.Sex==1][df.Survived==1].shape[0]
print(MaleS)
MaleN=df[df.Sex==1][df.Survived==0].shape[0]
print(MaleN)
FemaleS=df[df.Sex==0][df.Survived==1].shape[0]
print(FemaleS)
FemaleN=df[df.Sex==0][df.Survived==0].shape[0]
print(FemaleN)
chart=[MaleS,MaleN,FemaleS,FemaleN]
colors=['Green','Magenta','Gold','Silver']
labels=["Survived Male","Not Survived Male","Survived Female","Not Survived Female"]
explode=[0,0.05,0,0]
plt.pie(chart,labels=labels,colors=colors,explode=explode,startangle=1000,autopct="%.2f%%")
plt.axis("equal")
plt.show()
