#%%
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats

#%%
missing_flights = pd.read_json("flights_missing.json")
print(missing_flights)
#%%

missing_flights.head()
# missing_flights.filter(["manufacturer", "model","year", "hwy"])
# %%
missing_flights.to_markdown(index=False)

# %%

missing_flights.query("month == 'January'")
# %%

missing_flights.describe()
# %%

missing_flights['time_hour'] = pd.to_datetime(missing_flights.time_hour, format = "%Y-%m-%d %H:%M:%S")

# %%
