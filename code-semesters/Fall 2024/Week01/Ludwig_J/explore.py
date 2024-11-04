#%%
import polars as pl
import plotly.express as px
from lets_plot import *
LetsPlot.setup_html()
import numpy as np

#%%
places = pl.read_parquet("../data/parquet/places.parquet")
patterns = pl.read_parquet("../data/parquet/patterns.parquet")


# %%
patterns.select("placekey", "device_type")

#%%import numpy as np
from lets_plot import *
LetsPlot.setup_html()

np.random.seed(12)
data = dict(
    cond=np.repeat(['A', 'B'], 200),
    rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
)

background = element_rect(fill='#14181e')
ggplot(patterns.limit(100), aes(x='rating', fill='cond')) + ggsize(700, 300) + \
    geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') + \
    flavor_high_contrast_dark() + \
    theme(panel_grid_major_x='blank', plot_background=background, legend_background=background)
# %%
