#%%
import pandas as pd
import altair as alt
import numpy as np

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

"""Questions and Tasks
Which airport has the worst delays? Discuss the metric you chose, and why you chose it to determine the “worst” airport. Your answer should include a summary table that lists (for each airport) the total number of flights, total number of delayed flights, proportion of delayed flights, and average delay time in hours.

What is the best month to fly if you want to avoid delays of any length? Discuss the metric you chose and why you chose it to calculate your answer. Include one chart to help support your answer, with the x-axis ordered by month. (To answer this question, you will need to remove any rows that are missing the Month variable.)

According to the BTS website, the “Weather” category only accounts for severe weather delays. Mild weather delays are not counted in the “Weather” category, but are actually included in both the “NAS” and “Late-Arriving Aircraft” categories. Your job is to create a new column that calculates the total number of flights delayed by weather (both severe and mild). You will need to replace all the missing values in the Late Aircraft variable with the mean. Show your work by printing the first 5 rows of data in a table. Use these three rules for your calculations:__

100% of delayed flights in the Weather category are due to weather
30% of all delayed flights in the Late-Arriving category are due to weather.
From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.
Using the new weather variable calculated above, create a barplot showing the proportion of all flights that are delayed by weather at each airport. Discuss what you learn from this graph.

Fix all of the varied missing data types in the data to be consistent (all missing values should be displayed as “NaN”). In your report include one record example (one row) from your new data, in the raw JSON format. Your example should display the “NaN” for at least one missing value.__"""
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

chart3 = missing_flights.num_of_delays_weather_total.head()
# %%
chart3




# %%
# Create a new DataFrame with the weather variable
weather_df = missing_flights[['airport_code', 'num_of_delays_weather_total', 'num_of_flights_total']]

# Calculate the proportion of flights delayed by weather
weather_df['proportion_delayed_by_weather'] = weather_df['num_of_delays_weather_total'] / weather_df['num_of_flights_total']

# Create a barplot of the proportion of flights delayed by weather
barplot = alt.Chart(weather_df).mark_bar().encode(
    x='airport_code',
    y='proportion_delayed_by_weather',
    tooltip=['airport_code', 'proportion_delayed_by_weather']
).properties(
    title='Proportion of Flights Delayed by Weather at Each Airport',
    width=600,
    height=400
)

# Show the barplot
barplot.show()




# %%

missing_flights.replace('n/a', np.nan, inplace=True)
missing_flights.head()

# %%
