#!/usr/bin/env python
# coding: utf-8



import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
sns.set()
# sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'#cccccc'})
#get_ipython().run_line_magic('matplotlib', 'auto')
from PIL import Image
import pandas as pd



gB = 1.353
gG = 0.862
gR = 1.6543



df = pd.read_excel('cvalsw1.xlsx')




df.head()




# # linearize values.
# def linearizeRows(row):
#     row.r = 
# df.transform(linearizeRows, axis=1)




df.r = np.power(df.r.values, gR)
df.g = np.power(df.g.values, gG)
df.b = np.power(df.b.values, gB)




df.head()




# # normalize values.
def normalizeRows(row):
    total = row.r + row.g + row.b
    row.r = row.r / total
    row.g = row.g / total
    row.b = row.b / total
#     print(row.sq)
    if row.sq == 'w':
        row.sq = 'white'
    elif row.sq == 'c':
        row.sq = 'cyan'
    elif row.sq == 'm':
        row.sq = 'blue'
    else:
        row.sq = 'yellow'
#     print(row.sq)
        
    return row
df = df.transform(normalizeRows, axis=1)

df.head()

plt.figure(figsize=(10, 10))
plt.rcParams['axes.facecolor'] = '#f9f9f9'
plt.grid(color='#aaaaaa')
palette = {'white':'black', 'blue':'blue', 'yellow': 'yellow', 'cyan': 'cyan'}
ax = sns.scatterplot(df.r, df.g,  style=df.ill, hue=df.sq, markers={1:'X', 2:'o', 3:'*'}, palette=palette, s=100)
# plt.xlabel = 'R/(R+G+B)'
ax.set(xlabel='R/(R+G+B)', ylabel='G/(R+G+B)')
plt.show()


