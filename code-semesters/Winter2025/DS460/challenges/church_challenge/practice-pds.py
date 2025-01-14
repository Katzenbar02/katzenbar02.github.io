#%%
import polars as pl
import json
import plotly.express as px

# Load the data from the uploaded CSV files
file_path_1 = '2022-01-13-19-2021-10-core_poi-patterns.csv'
file_path_2 = '2022-01-13-19-2021-11-core_poi-patterns.csv'
file_path_3 = '2022-01-13-19-2021-12-core_poi-patterns.csv'

# Loading the datasets into Polars dataframes
df1 = pl.read_csv(file_path_1)
df2 = pl.read_csv(file_path_2)
df3 = pl.read_csv(file_path_3)

# Combine the dataframes for analysis
combined_df = pl.concat([df1, df2, df3])

#%% Question 1: Differences between iPhone and Android users
lds_churches = combined_df.filter(combined_df['location_name'].str.contains("Church of Jesus Christ"))

# Convert 'device_type' from JSON string to dictionary
device_type_parsed = [json.loads(x) if x else {"android": 0, "ios": 0} for x in lds_churches['device_type']]
lds_churches = lds_churches.with_columns(pl.Series(name='device_type', values=device_type_parsed))

# Extract the state information from 'poi_cbg' (casting to string first)
lds_churches = lds_churches.with_columns(lds_churches['poi_cbg'].cast(pl.Utf8).str.slice(0, 2).alias('state'))

# Filter for Utah and Georgia
lds_utah_georgia = lds_churches.filter(lds_churches['state'].is_in(['49', '13']))

# Extract android and ios visits from 'device_type'
android_visits = [x.get('android', 0) for x in lds_utah_georgia['device_type']]
ios_visits = [x.get('ios', 0) for x in lds_utah_georgia['device_type']]
lds_utah_georgia = lds_utah_georgia.with_columns([
    pl.Series(name='android_visits', values=android_visits),
    pl.Series(name='ios_visits', values=ios_visits)
])

# Grouping by state and calculating total visits for Android and iOS
device_summary = lds_utah_georgia.group_by('state').agg([
    pl.sum('android_visits').alias('android_visits'),
    pl.sum('ios_visits').alias('ios_visits')
])

# Update the state codes to state names
device_summary = device_summary.with_columns(
    device_summary['state'].apply(lambda x: 'Utah' if x == '49' else 'Georgia').alias('state')
)

# Plotting the comparison using Plotly
fig = px.bar(device_summary.to_pandas(), x='state', y=['android_visits', 'ios_visits'],
             title='Comparison of Visits to LDS Buildings by Device Type in Utah and Georgia',
             labels={'value': 'Number of Visits', 'state': 'State'}, barmode='group')
fig.update_layout(legend_title_text='Device Type')
fig.show()

#%% Question 2: Hourly usage patterns for LDS vs. other churches in Utah and Georgia
lds_churches = lds_churches.with_columns(lds_churches['popularity_by_day'].apply(lambda x: json.loads(x) if x else {}).alias('popularity_by_day'))
other_churches = combined_df.filter(~combined_df['location_name'].str.contains("Church of Jesus Christ", case=False))
other_churches = other_churches.filter(other_churches['top_category'] == 'Religious Organizations')
other_churches = other_churches.with_columns(other_churches['poi_cbg'].str.slice(0, 2).alias('state'))

# Filter for Utah and Georgia churches
lds_utah_georgia = lds_churches.filter(lds_churches['state'].is_in(['49', '13']))
other_utah_georgia = other_churches.filter(other_churches['state'].is_in(['49', '13']))

# Initialize dictionaries to store hourly data for LDS and other churches in Utah and Georgia
hourly_usage = {
    'Utah_LDS': {hour: 0 for hour in range(24)},
    'Utah_Other': {hour: 0 for hour in range(24)},
    'Georgia_LDS': {hour: 0 for hour in range(24)},
    'Georgia_Other': {hour: 0 for hour in range(24)}
}

# Sum up the usage for each day of the week to get hourly usage for the whole week
for row in lds_utah_georgia.iter_rows(named=True):
    state = 'Utah' if row['state'] == '49' else 'Georgia'
    for day, hours in row['popularity_by_day'].items():
        if isinstance(hours, list):
            for hour, count in enumerate(hours):
                hourly_usage[f'{state}_LDS'][hour] += count

for row in other_utah_georgia.iter_rows(named=True):
    state = 'Utah' if row['state'] == '49' else 'Georgia'
    for day, hours in row['popularity_by_day'].items():
        if isinstance(hours, list):
            for hour, count in enumerate(hours):
                hourly_usage[f'{state}_Other'][hour] += count

# Convert the dictionaries to DataFrames for plotting
hourly_usage_utah_combined_df = pl.DataFrame({
    'Hour': list(range(24)),
    'Total_Visits_Utah_LDS': list(hourly_usage['Utah_LDS'].values()),
    'Total_Visits_Utah_Other': list(hourly_usage['Utah_Other'].values())
})

hourly_usage_georgia_combined_df = pl.DataFrame({
    'Hour': list(range(24)),
    'Total_Visits_Georgia_LDS': list(hourly_usage['Georgia_LDS'].values()),
    'Total_Visits_Georgia_Other': list(hourly_usage['Georgia_Other'].values())
})

# Plotting the combined hourly usage patterns for Utah and Georgia using Plotly
fig_utah = px.bar(hourly_usage_utah_combined_df.to_pandas(), x='Hour',
                  y=['Total_Visits_Utah_LDS', 'Total_Visits_Utah_Other'],
                  title='Hourly Church Usage in Utah: LDS vs. Other Churches',
                  labels={'value': 'Total Visits', 'Hour': 'Hour of the Day'}, barmode='group')
fig_utah.update_layout(legend_title_text='Church Type')
fig_utah.show()

fig_georgia = px.bar(hourly_usage_georgia_combined_df.to_pandas(), x='Hour',
                     y=['Total_Visits_Georgia_LDS', 'Total_Visits_Georgia_Other'],
                     title='Hourly Church Usage in Georgia: LDS vs. Other Churches',
                     labels={'value': 'Total Visits', 'Hour': 'Hour of the Day'}, barmode='group')
fig_georgia.update_layout(legend_title_text='Church Type')
fig_georgia.show()

#%% Question 3: Related brands comparison between LDS and other churches
lds_utah = lds_utah_georgia.filter(lds_utah_georgia['state'] == '49')
other_churches_utah = other_utah_georgia.filter(other_utah_georgia['state'] == '49')
lds_utah = lds_utah.with_columns(lds_utah['related_same_day_brand'].apply(lambda x: json.loads(x) if x else {}).alias('related_same_day_brand'))
other_churches_utah = other_churches_utah.with_columns(other_churches_utah['related_same_day_brand'].apply(lambda x: json.loads(x) if x else {}).alias('related_same_day_brand'))

# Aggregating related brands for LDS churches
related_brands_utah = {}
for brand_data in lds_utah['related_same_day_brand']:
    for brand, count in brand_data.items():
        if brand in related_brands_utah:
            related_brands_utah[brand] += count
        else:
            related_brands_utah[brand] = count

related_brands_utah_df = pl.DataFrame(list(related_brands_utah.items()), columns=['Brand', 'Count_LDS']).sort('Count_LDS', descending=True).head(10)

# Aggregating related brands for other churches
related_brands_other_utah = {}
for brand_data in other_churches_utah['related_same_day_brand']:
    for brand, count in brand_data.items():
        if brand in related_brands_other_utah:
            related_brands_other_utah[brand] += count
        else:
            related_brands_other_utah[brand] = count

related_brands_other_utah_df = pl.DataFrame(list(related_brands_other_utah.items()), columns=['Brand', 'Count_Other']).sort('Count_Other', descending=True).head(10)

# Plotting related brands for LDS vs. other churches using Plotly
fig_utah_related = px.bar(related_brands_utah_df.to_pandas(), x='Brand', y='Count_LDS',
                          title='Top Related Brands for LDS Churches in Utah',
                          labels={'Count_LDS': 'Visit Count', 'Brand': 'Brand'})
fig_utah_related.update_layout(xaxis_tickangle=45)
fig_utah_related.show()

fig_other_related = px.bar(related_brands_other_utah_df.to_pandas(), x='Brand', y='Count_Other',
                           title='Top Related Brands for Other Churches in Utah',
                           labels={'Count_Other': 'Visit Count', 'Brand': 'Brand'}, color_discrete_sequence=['orange'])
fig_other_related.update_layout(xaxis_tickangle=45)
fig_other_related.show()

#%% Question 4: Related brands for temples, seminaries, and meetinghouses
lds_temples = combined_df.filter(combined_df['location_name'].str.contains("Temple", case=False))
lds_seminary = combined_df.filter(combined_df['location_name'].str.contains("Seminary", case=False))
lds_meetinghouses = combined_df.filter(
    combined_df['location_name'].str.contains("Church of Jesus Christ", case=False) &
    ~combined_df['location_name'].str.contains("Temple|Seminary", case=False)
)

# Extract related brands for temples, seminaries, and meetinghouses
lds_temples = lds_temples.with_columns(lds_temples['related_same_day_brand'].apply(lambda x: json.loads(x) if x else {}).alias('related_same_day_brand'))
lds_seminary = lds_seminary.with_columns(lds_seminary['related_same_day_brand'].apply(lambda x: json.loads(x) if x else {}).alias('related_same_day_brand'))
lds_meetinghouses = lds_meetinghouses.with_columns(lds_meetinghouses['related_same_day_brand'].apply(lambda x: json.loads(x) if x else {}).alias('related_same_day_brand'))

# Aggregate related brands for temples
related_brands_temples = {}
for brand_data in lds_temples['related_same_day_brand']:
    for brand, count in brand_data.items():
        if brand in related_brands_temples:
            related_brands_temples[brand] += count
        else:
            related_brands_temples[brand] = count

related_brands_temples_df = pl.DataFrame(list(related_brands_temples.items()), columns=['Brand', 'Count_Temples']).sort('Count_Temples', descending=True).head(10)

# Aggregate related brands for seminary buildings
related_brands_seminary = {}
for brand_data in lds_seminary['related_same_day_brand']:
    for brand, count in brand_data.items():
        if brand in related_brands_seminary:
            related_brands_seminary[brand] += count
        else:
            related_brands_seminary[brand] = count

related_brands_seminary_df = pl.DataFrame(list(related_brands_seminary.items()), columns=['Brand', 'Count_Seminary']).sort('Count_Seminary', descending=True).head(10)

# Aggregate related brands for meetinghouses
related_brands_meetinghouses = {}
for brand_data in lds_meetinghouses['related_same_day_brand']:
    for brand, count in brand_data.items():
        if brand in related_brands_meetinghouses:
            related_brands_meetinghouses[brand] += count
        else:
            related_brands_meetinghouses[brand] = count

related_brands_meetinghouses_df = pl.DataFrame(list(related_brands_meetinghouses.items()), columns=['Brand', 'Count_Meetinghouses']).sort('Count_Meetinghouses', descending=True).head(10)

# Plotting related brands for temples, seminaries, and meetinghouses using Plotly
fig_temples = px.bar(related_brands_temples_df.to_pandas(), x='Brand', y='Count_Temples',
                     title='Top Related Brands for Temples',
                     labels={'Count_Temples': 'Visit Count', 'Brand': 'Brand'}, color_discrete_sequence=['purple'])
fig_temples.update_layout(xaxis_tickangle=45)
fig_temples.show()

fig_seminary = px.bar(related_brands_seminary_df.to_pandas(), x='Brand', y='Count_Seminary',
                      title='Top Related Brands for Seminary Buildings',
                      labels={'Count_Seminary': 'Visit Count', 'Brand': 'Brand'}, color_discrete_sequence=['blue'])
fig_seminary.update_layout(xaxis_tickangle=45)
fig_seminary.show()

fig_meetinghouses = px.bar(related_brands_meetinghouses_df.to_pandas(), x='Brand', y='Count_Meetinghouses',
                           title='Top Related Brands for Meetinghouses',
                           labels={'Count_Meetinghouses': 'Visit Count', 'Brand': 'Brand'}, color_discrete_sequence=['green'])
fig_meetinghouses.update_layout(xaxis_tickangle=45)
fig_meetinghouses.show()
