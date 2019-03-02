import numpy as np
import pandas as pd
train = pd.read_csv('C:/Users/bhava/OneDrive/Documents/python/ICP6/Python_Lesson6/train.csv')

print ("Train data shape:", train.shape)
import matplotlib.pyplot as plt

var ='GarageArea'
data = pd.concat([train['SalePrice'], train[var]], axis = 1)
plt.scatter(x=train['GarageArea'], y=train['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above grade (ground) living area square feet')
plt.show()

from scipy import stats
z = np.abs(stats.zscore(data))
print(z)
threshold=3
print(np.where(z>3))

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


data = data[(z < 3).all(axis=1)]



var ='GarageArea'
plt.scatter(x=data['GarageArea'], y=data['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above grade (ground) living area square feet')
plt.show()
