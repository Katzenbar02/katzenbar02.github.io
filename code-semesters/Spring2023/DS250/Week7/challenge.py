#%%
import pandas as pd
import altair as alt
import numpy as np


#%%
data = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')


# %%
data
# %%
data.head()

#%%
joshuaChart = alt.Chart(data, title="AWWWWW").mark_square(clip=True).encode(
    alt.X("hp", title="Horse Power",scale=alt.Scale(domain=(0, 180))),
    alt.Y("mpg", title="Miles per Gallon")
).properties(width=400, height=300).configure_mark(
    color='red'
)
# %%
joshuaChart
# %%
