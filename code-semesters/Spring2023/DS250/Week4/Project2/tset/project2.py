# %%

import pandas as pd
import numpy as np

import json
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json"
JSON = pd.read_json(url)

JSON['hours_delayed_total'] = JSON['minutes_delayed_total'] / 60

JSON['proportion'] = JSON['num_of_delays_total'] / JSON['num_of_flights_total']

chart1 = JSON.groupby('airport_code').sum().filter(items=['num_of_flights_total','num_of_delays_total', 'proportion', 'hours_delayed_total'])

chart1

removed = JSON[JSON["month"] != "n/a"]
# This removes any n/a in the "month" column

removed['month'] = removed['month'].replace('Febuary', 'February')
# February was spelled wrong, so this corrected it

month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# This places the months in order

removed['month'] = pd.Categorical(removed['month'], categories=month_order, ordered=True)
# This categorized the month order

chart2 = removed.groupby(by='month').sum().filter(items=['num_of_flights_total','num_of_delays_total', 'proportion'])
# This grouped up the rows by months

chart2

# %%


chart4 = JSON.tot_num_of_weather_delays.groupby('airport_code')

source = chart4({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)
# %%
