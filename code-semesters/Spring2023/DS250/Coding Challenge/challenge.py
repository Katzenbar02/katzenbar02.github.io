# %%
import altair as alt
import pandas as pd
import numpy as np
import matplotlib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


# Question|Task 1: Chart
#%%
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv" 
names = pd.read_csv(url)

#%%
Kobe = names.query("name == 'Kobe'")[["name", "year", 'Total']]
print(Kobe)

#%%
kobeChart = alt.Chart(Kobe, title="Kobe Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1970, 2015))),
    alt.Y("Total", title="Total")
).properties(width=400, height=300)

kobeChart


#%% Question|Task 2: Dealing with Missing Data
steve = pd.DataFrame({"steve": ['N/A', 15, 22, 45, 31, -999, 21, 2, 0, 0, 0, 'broken', 19, 19, 36, 27, 0, np.nan, 0, 33, 42, -999]})

#%% Step 1: Replace unofficial missing values with Python-recognized missing values
steve.replace(['N/A', 'broken', -999], np.nan, inplace=True)

#%% Step 2: Replace missing values with the average excluding zeros
non_zero_mean = steve[steve != 0].mean()
steve.replace(0, np.nan, inplace=True)
steve.fillna(non_zero_mean, inplace=True)

#%% Step 3: Report the mean and standard deviation of the cleaned data (including the zeros)
mean_with_zeros = steve.mean()
std_with_zeros = steve.std()

#%%
print("Mean (including zeros):", mean_with_zeros)
print("Standard Deviation (including zeros):", std_with_zeros)

#%% Question|Task 3: Histogram Chart
# Reproduce this histogram of the cleaned data including the zeros from Q|T2.
# Use the clean star wars data to predict if someone is a female by how they responded to the surevey questions
# Report your accuracy and a feature importance plot with the top 25 most important features.
# Use test_size = .20 and random_state = 2022 in train_test_split()
# Use the RandomForestClassifier(random_state = 2022) method.
#%%
steveChart = alt.Chart(steve, title="Steve's Data").mark_bar().encode(
    alt.X("steve", bin=alt.Bin(maxbins=20), title="Steve"),
    alt.Y("count()", title="Count of Records")
).properties(width=400, height=300)

steveChart

# %% Question|Task 4: Machine Learning
# Use the clean star wars data to predict if someone is a female by how they responded to the surevey questions
# Report your accuracy and a feature importance plot with the top 25 most important features.
# Use test_size = .20 and random_state = 2022 in train_test_split()
# Use the RandomForestClassifier(random_state = 2022) method.

#%%
url = "http://byuistats.github.io/CSE250-Course/data/clean_starwars.csv"
sw_dat = pd.read_csv(url)

sw_dat.gender.value_counts()

#%%
sw_dat.replace(['Yes', 'No'], [1, 0], inplace=True)

#%%
# Use the clean star wars data to predict if someone is a female by how they responded to the surevey questions



