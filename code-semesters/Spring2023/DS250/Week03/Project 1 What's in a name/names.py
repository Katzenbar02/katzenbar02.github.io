
#%%
import numpy as np
import altair as alt
import pandas as pd

#%%
names = pd.read_csv('names_year.csv')
# %%

#%%
# Filter the DataFrame to include only rows where the name contains "Oliver"
oliver_names = names.query('name == "Oliver"')[['name','UT']]
total_olivers = oliver_names['UT'].sum()
#%%
print(total_olivers)
#%%
print(oliver_names)

# %%
