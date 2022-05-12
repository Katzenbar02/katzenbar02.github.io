#%%
from cmath import nan
import pandas as pd
import altair as alt
import numpy as np

# %%from url to pandas dataframe
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)


# %%

cars.head()

# %%

print(cars)

# %%
cars.query("car == ''").count()
# %%
cars.car.value_counts()
# %%
cars.dropna()
# %%
recar = cars.replace(999, np.nan)
# %%
cars
# %%
recar.replace(np.nan,'junk')

# %%
print(cars.groupby('cyl').agg(mean_weight = ('wt', np.mean)).reset_index().to_markdown(index = False))

# %%
cars.replace(999,np.nan,inplace=True)
cars
# %%

cars.wt.replace(np,nan, 2.40375)