
#%%
import numpy as np
import altair as alt
import pandas as pd

#%%
names = pd.read_csv('names_year.csv')



# %%
Joshua = names.query("name == 'Joshua'")[["name", "year", 'Total']]
print(Joshua)
 #%%
joshuaChart = alt.Chart(Joshua, title="Joshua Popularity").mark_line(clip=True).encode(
    alt.X("year", title="Year",scale=alt.Scale(domain=(1970, 2015))),
    alt.Y("Total", title="Total")
).properties(width=400, height=300)

joshuaChart
#%%

# %%
