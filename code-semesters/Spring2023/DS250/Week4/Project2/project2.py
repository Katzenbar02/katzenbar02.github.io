#%%
import pandas as pd
import altair as alt
import numpy as np
from scipy import stats

# ALL VARIABLES USED: airport_code	character	Airport Code
"""
airport_name	character	Airport Name
month	character	Month
year	integer	Year
num_of_flights_total	integer	Num Of Flights Total
num_of_delays_carrier	character	Num Of Delays Carrier
num_of_delays_late_aircraft	integer	Num Of Delays Late Aircraft
num_of_delays_nas	integer	Num Of Delays Nas
num_of_delays_security	integer	Num Of Delays Security
num_of_delays_weather	integer	Num Of Delays Weather
num_of_delays_total	integer	Num Of Delays Total
minutes_delayed_carrier	integer	Minutes Delayed Carrier
minutes_delayed_late_aircraft	integer	Minutes Delayed Late Aircraft
minutes_delayed_nas	integer	Minutes Delayed Nas
minutes_delayed_security	integer	Minutes Delayed Security
minutes_delayed_weather	integer	Minutes Delayed Weather
minutes_delayed_total	integer	Minutes Delayed Total
"""
#%%
missing_flights = pd.read_json("flights_missing.json")

missing_flights['hours_delayed_total'] = missing_flights['minutes_delayed_total'] / 60

missing_flights['proportion_delayed'] = missing_flights['num_of_delays_total'] / missing_flights['num_of_flights_total']
# Find the airport with the highest total hours of delay
worst_airport = missing_flights.loc[missing_flights['hours_delayed_total'].idxmax()]

chart1 = missing_flights.groupby('airport_code').sum().filter(items=['num_of_flights_total', 'number_of_delays_total', 'proportion_delayed', 'hours_delayed_total'])
#%%
chart1
#%%
remove_month = missing_flights[missing_flights["month"] != "n/a"]
# This removes any n/a in the "month" column

remove_month['month'] = remove_month['month'].replace('Febuary', 'February')

month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

remove_month['month'] = pd.Categorical(remove_month['month'], categories=month_order, ordered=True)

chart2 = remove_month.groupby(by='month').sum().filter(items=['num_of_flights_total', 'num_of_delays_total', 'proportion_delayed'])
#%%
chart2
# %%
# Step 1: Replace missing values in the "num_of_delays_late_aircraft" column with the mean
mean_late_aircraft = missing_flights['num_of_delays_late_aircraft'].mean()
missing_flights['num_of_delays_late_aircraft'].fillna(mean_late_aircraft, inplace=True)

# Step 2: Create a new column "num_of_delays_weather_total" initialized with zeros
missing_flights['num_of_delays_weather_total'] = 0

# Step 3: Apply the rules to calculate the values for "num_of_delays_weather_total" column
# Rule 1: 100% of delayed flights in the Weather category are due to weather
missing_flights.loc[missing_flights['num_of_delays_weather'].notnull(), 'num_of_delays_weather_total'] = missing_flights['num_of_delays_weather']

# Rule 2: 30% of all delayed flights in the Late-Arriving category are due to weather
missing_flights['num_of_delays_weather_total'] += 0.3 * missing_flights['num_of_delays_late_aircraft']

# Rule 3: From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.
missing_flights.loc[missing_flights['month'].isin(['April', 'May', 'June', 'July', 'August']), 'num_of_delays_weather_total'] += 0.4 * missing_flights['num_of_delays_nas']
missing_flights.loc[~missing_flights['month'].isin(['April', 'May', 'June', 'July', 'August']), 'num_of_delays_weather_total'] += 0.65 * missing_flights['num_of_delays_nas']

# Print the first 5 rows of the updated table
print(missing_flights.head(5))
# replace all the missing values in the Late Aircraft variable with the mean of the column

#%%
# create a new column that calculates the total number of weather delays for each airport
missing_flights['total_weather_delays'] = missing_flights['weather_ct'] + missing_flights['nas_ct'] + missing_flights['late_aircraft_ct']

# Group the data by airport code and calculate the proportion of flights delayed by weather
weather_proportions = missing_flights.groupby('airport_code')['num_of_delays_weather_total'].sum() / missing_flights.groupby('airport_code')['num_of_flights_total'].sum()
weather_proportions = weather_proportions.reset_index()

# Create the bar plot using Altair
bar_plot = alt.Chart(weather_proportions).mark_bar().encode(
    x='airport_code',
    y='num_of_delays_weather_total',
    tooltip=['airport_code', 'num_of_delays_weather_total']
).properties(
    title='Proportion of Flights Delayed by Weather at Each Airport',
    width=600,
    height=400
)

# Show the bar plot
bar_plot.show()

#%%
chart4 = missing_flights.weather_proporions.groupby('airport_code')

source = chart4({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)

#%%
missing_flights = pd.read_json("flights_missing.json").fillna(np.nan)
missing_flights.replace('n/a', np.nan, inplace=True)
missing_flights.replace('na', np.nan, inplace=True)
missing_flights.replace('N/A', np.nan, inplace=True)
missing_flights.replace('NA', np.nan, inplace=True)
missing_flights.replace('missing', np.nan, inplace=True)




# Creates a new column that calculates the total number of weather delays
# for each airport

# missing_flights['total_weather_delays'] = missing_flights['weather_ct'] + missing_flights['nas_ct'] + missing_flights['late_aircraft_ct']

# missing_flights['late_aircraft_ct'] = missing_flights['late_aircraft_ct'].fillna(missing_flights['late_aircraft_ct'].mean())

# # Step 2: Calculate the total number of weather delays based on the specified rules
# is_severe_weather = missing_flights['weather_ct']
# is_late_arriving_weather = missing_flights['late_aircraft_ct'] * 0.3
# is_nas_weather = np.where(remove_month['month'].isin(['April', 'May', 'June', 'July', 'August']),
#                           missing_flights['nas_ct'] * 0.4,
#                           missing_flights['nas_ct'] * 0.65)

# missing_flights['total_weather_delays'] = is_severe_weather + is_late_arriving_weather + is_nas_weather

# # Print the first 5 rows of data with the new column
# print(missing_flights.head(5))
# # %%
# tot_num_of_weather_delays = missing_flights['carrier_ct'] + missing_flights['weather_ct'] + missing_flights['nas_ct'] + missing_flights['security_ct'] + missing_flights['late_aircraft_ct']
# chart4 = missing_flights.tot_num_of_weather_delays.groupby('airport_code') 

# %%

missing_flights
# %%
