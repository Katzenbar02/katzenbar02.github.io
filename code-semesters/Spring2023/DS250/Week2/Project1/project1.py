#%%
import pandas as pd
import altair as alt
import numpy as np


#%%
names = pd.read_csv("names_year.csv")




# GRAND QUESTION 1
# %% Joshua query
Joshua = names.query("name == 'Joshua'")[["name", "year", 'Total']]
print(Joshua)

#%% Joshua Names

joshuaChart = alt.Chart(Joshua, title="Joshua Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1970, 2015))),
    alt.Y("Total", title="Total")
).properties(width=400, height=300)

joshuaChart

# %% Save Joshua Chart

joshuaChart.save("joshua_chart.png")

#%% Joshua Table code
table = Joshua.head(83)
print(table.to_markdown())





# GRAND QUESTION 2
# %% Create Brittany query

Brittany = names.query("name == 'Brittany'")[["name", "year", 'Total']]
print(Brittany)

#%% Brittany Names

brittanyChart = alt.Chart(Brittany, title="Brittany Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1975, 2015))),
    alt.Y("Total", title="Total")
).properties(width=400, height=300)

brittanyChart
# %% Save Brittany Chart

brittanyChart.save("brittany_chart.png")

#%% Brittany Table code
table = Brittany.head(31)
print(table.to_markdown())




# GRAND QUESTION 3
# %% Create Mary, Martha, Peter, and Paul From 1920 - 2000
# allBilble = ["Mary", "Martha", "Peter", "Paul"]
Bible =  names.query('name in ["Mary", "Martha", "Peter", "Paul"]')[["name", "year", 'Total']]
print(Bible)
#%% Bible Names

bibleChart = alt.Chart(Bible, title="Bible Name Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1920, 2000))),
    alt.Y("Total", title="Total"),
    color = 'name')
    
    # .transform_filter(
    # alt.FieldOneOfPredicate(field='name', oneOf=['Mary', 'Martha', 'Peter'])


bibleChart
#%% Save bible Chart

bibleChart.save("bible_chart.png")

#%% Bible Table code
table = Bible.head(42)
print(table.to_markdown())



# GRAND QUESTION 4
# %%# Anakin query
Anakin = names.query("name == 'Anakin'")[["name", "year", 'Total']]
print(Anakin)

#%% Anakin Names

anakinChart = alt.Chart(Anakin, title="Anakin Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1998, 2015))),
    alt.Y("Total", title="Total")
).properties(width=400, height=300)

anakinChart
# %% Save Harry Chart

anakinChart.save("anakin_chart.png")

#%% Anakin Table code
table = Anakin.head(42)
print(table.to_markdown())





# %% Create Mary, Martha, Peter, and Paul From 1920 - 2000
# allBilble = ["Mary", 'Martha', 'Peter', 'Paul']
State1 = "TX"
State2 = "MD"
State3 = "IL"
grand = State1 + State2 + State3
friends =  names.query('name in ["Luke", "Joshua", "Nathalie"]')[["name", "year",State1, State2, State3, 'Total']]
print(friends)
#%% Bible Names

friendChart = alt.Chart(friends, title="Bible Name Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1970, 2015))),
    alt.Y("Total", title="Total"),
    color = 'name')
    
    # .transform_filter(
    # alt.FieldOneOfPredicate(field='name', oneOf=['Mary', 'Martha', 'Peter'])


friendChart

# %%

