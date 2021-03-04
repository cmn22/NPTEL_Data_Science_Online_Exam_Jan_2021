import os
import pandas as pd
import numpy as np

os.chdir("C:/Users/chait/Desktop")

df = pd.read_csv('apy.csv', index_col=0)

# QUESTION 1
# ----------
# season = df.groupby('Season')

# kharif = season.get_group('Kharif     ')
# print('Kharif Production: ', kharif['Production'].aggregate(np.sum))

# summer = season.get_group('Summer     ')
# print('Summer Production: ', summer['Production'].aggregate(np.sum))

# autumn = season.get_group('Autumn     ')
# print('Autumn Production: ', autumn['Production'].aggregate(np.sum))



# QUESTION 2
# ----------
# season = df.groupby('Season')
# kharif = season.get_group('Kharif     ')
# print(np.unique(kharif['Crop']))



# QUESTION 3
# ----------
# import operator

# districts = np.unique(df['District_Name'])

# district_production = dict()

# for district in districts:
#     district_production_total = df[df['District_Name']==district]['Production'].aggregate(np.sum)
#     district_production[district] = district_production_total

# descending_district_production = dict(sorted(district_production.items(), key=operator.itemgetter(1),reverse=True))
# print(descending_district_production)

# ascending_district_production = dict(sorted(district_production.items(), key=lambda item: item[1]))
# print(ascending_district_production)



# QUESTION 4
# ----------
# tamil_nadu = df[df['State_Name'] == 'Tamil Nadu']

# years_group = tamil_nadu.groupby('Crop_Year')

# years = np.unique(tamil_nadu['Crop_Year'])

# yearly_production = dict()

# for yr in years:  
#     yearly_production[yr] = years_group.get_group(yr)['Production'].aggregate(np.sum)
    
# ascending_yearly_production = dict(sorted(yearly_production.items(), key=lambda item: item[1]))
# print(ascending_yearly_production)



# QUESTION 5
# ----------
# state_names = np.unique(df['State_Name'])

# state_groups = df.groupby('State_Name')

# state_production = dict()

# for state in state_name:   
#     state_production[state] = state_groups.get_group(state)['Production'].aggregate(np.sum)
    
# ascending_state_production = dict(sorted(state_production.items(), key=lambda item: item[1]))
# print(ascending_state_production)

# OR

# df.groupby('State Name')['Production'].sum().sort_values(ascending = False)



# QUESTION 6
# ----------
# TO BE DONE



# QUESTION 7
# ----------
# print(df['Production'].aggregate(np.mean))



# QUESTION 8
# ----------
# print(df['Production'].aggregate(np.std))



# QUESTION 9
# ----------
# yr_2015 = df[df['Crop_Year'] == 2015]
# print(np.unique(yr_2015['State_Name']))



# QUESTION 10
# -----------
# yr_1997 = df[df['Crop_Year'] == 1997]

# print(yr_1997.groupby('Crop')['Production'].sum().sort_values(ascending = False))



# QUESTION 11
# -----------
# TO BE DONE



# QUESTION 12
# -----------
# print(df.groupby('Crop_Year')['Production'].sum().sort_values(ascending = False))



# QUESTION 13
# -----------
# tamil_nadu = df[df['State_Name'] == 'Tamil Nadu']

# print(tamil_nadu.groupby('Crop')['Production'].sum().sort_values(ascending = False))

