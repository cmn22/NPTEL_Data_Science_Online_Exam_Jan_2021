import os
import pandas as pd
import numpy as np

import operator

os.chdir("C:/Users/chait/Desktop")

df = pd.read_csv('apy.csv')

# QUESTION 1
# ----------
# season = df.groupby('Season')
# autumn = season.get_group('Autumn     ')
# print(np.unique(autumn['Crop']))



# QUESTION 2
# ----------
# uttar_pradesh = df[df['State_Name'] == 'Uttar Pradesh']

# years_group = uttar_pradesh.groupby('Crop_Year')

# years = np.unique(uttar_pradesh['Crop_Year'])

# yearly_production = dict()

# for yr in years:  
#     yearly_production[yr] = years_group.get_group(yr)['Production'].aggregate(np.sum)
    
# ascending_yearly_production = dict(sorted(yearly_production.items(), key=lambda item: item[1]))
# print(ascending_yearly_production)



# QUESTION 3
# ----------
# df.groupby('Crop_Year')['Area'].sum().sort_values(ascending = True)



# QUESTION 4
# ----------
# df.groupby('State_Name')['Production'].sum().sort_values(ascending = True)



# QUESTION 5
# ----------
# yr_2015 = df[df['Crop_Year'] == 2015]

# print(yr_2015.groupby('Crop')['Production'].sum().sort_values(ascending = False))



# QUESTION 6
# ----------
# print(df['Area'].aggregate(np.std))



# QUESTION 7
# ----------
# mp = df[df['State_Name'] == 'Madhya Pradesh']

# print(mp.groupby('Crop')['Production'].sum().sort_values(ascending = False))



# QUESTION 8
# ----------
# season = df.groupby('Season')

# kharif = season.get_group('Kharif     ')
# print('Kharif Production: ', kharif['Production'].aggregate(np.sum))

# summer = season.get_group('Summer     ')
# print('Summer Production: ', summer['Production'].aggregate(np.sum))

# autumn = season.get_group('Autumn     ')
# print('Autumn Production: ', autumn['Production'].aggregate(np.sum))



# QUESTION 9
# ----------
# df.groupby('State_Name')['Area'].sum().sort_values(ascending = False)



# QUESTION 10
# -----------
# print(df['Area'].aggregate(np.mean))



# QUESTION 11
# -----------
# df.corr(method='pearson')



# QUESTION 12
# -----------
# print(df.groupby('Crop')['Production'].sum().sort_values(ascending = False))



# QUESTION 13
# -----------
# autumn = df[df['Season'] == 'Autumn     ']
# summer = df[df['Season'] == 'Summer     ']
# winter = df[df['Season'] == 'Winter     ']

# print(winter.groupby('Crop')['Production'].sum().sort_values(ascending = False))
