#%%
import polars as pl
import plotly.express as px
import json

# Load data from parquet files
data_paths = [
    "2022-01-13-19-2021-10-core_poi-patterns.csv",
    "2022-01-13-19-2021-11-core_poi-patterns.csv",
    "2022-01-13-19-2021-12-core_poi-patterns.csv"
]

# Combine data from multiple files
dataframes = [pl.read_csv(path) for path in data_paths]
df = pl.concat(dataframes)

# %%
# Filter data for Utah and Georgia
utah_georgia = df.filter(pl.col("region").is_in(["UT", "GA"]))

# Aggregate data by region
region_summary = utah_georgia.group_by("region").agg([
    pl.col("raw_visit_counts").sum().alias("total_visits")
])

# Convert to Pandas for Plotly visualization
region_summary_df = region_summary.to_pandas()

# Visualization
fig1 = px.bar(
    region_summary_df,
    x="region",
    y="total_visits",
    title="Total Visits in Utah and Georgia",
    labels={"total_visits": "Total Visits", "region": "State"}
)
fig1.show()

#%%
df_cleaned = df.drop_nulls(subset=['device_type', 'raw_visit_counts', 'popularity_by_hour', 'related_same_day_brand'])

# Filter data for hourly patterns
df_hourly = df_cleaned.filter(
    (df_cleaned['top_category'] == 'Religious Organizations') & 
    (df_cleaned['region'].is_in(['UT', 'GA']))
)

# Extract only the needed columns
df_hourly = df_hourly.select(['region', 'location_name', 'popularity_by_hour', 'related_same_day_brand'])

# Convert 'popularity_by_hour' from string to list of integers using Python's json.loads
hourly_data = []

for row in df_hourly.iter_rows():
    region = row[0]
    location_name = row[1]
    popularity_str = row[2]
    related_same_day_brand = row[3]

    try:
        # Convert the JSON-like string to a Python dictionary
        popularity_dict = json.loads(popularity_str)

        # Append data for each hour
        for hour, count in enumerate(popularity_dict):
            hourly_data.append({
                'region': region,
                'location_name': location_name,
                'hour': hour,
                'visit_count': popularity_dict[hour],
                'related_same_day_brand': related_same_day_brand
            })
    except (json.JSONDecodeError, TypeError):
        # Handle any parsing errors or if the value is null by skipping the problematic row
        continue

# Create a new Polars DataFrame from the transformed hourly data
df_hourly_transformed = pl.DataFrame(hourly_data)

# Separate Church of Jesus Christ and other churches
df_church = df_hourly_transformed.filter(df_hourly_transformed['location_name'] == 'The Church Of Jesus Christ Of Latter Day Saints')
df_other_church = df_hourly_transformed.filter(df_hourly_transformed['location_name'] != 'The Church Of Jesus Christ Of Latter Day Saints')

# Group by hour and region for both datasets
church_hourly_summary = df_church.group_by(['region', 'hour']).agg(pl.col('visit_count').sum().alias('total_visits'))
other_church_hourly_summary = df_other_church.group_by(['region', 'hour']).agg(pl.col('visit_count').sum().alias('total_visits'))

# Convert to Pandas for visualization
church_hourly_summary_pd = church_hourly_summary.to_pandas()
other_church_hourly_summary_pd = other_church_hourly_summary.to_pandas()

# Visualize hourly usage using scatter plot for other churches for better clarity
fig3 = px.scatter(church_hourly_summary_pd, x='hour', y='total_visits', color='region', title='Hourly Visits: Church of Jesus Christ')
fig4 = px.scatter(other_church_hourly_summary_pd, x='hour', y='total_visits', color='region', title='Hourly Visits: Other Churches')

# Display charts
fig3.show()
fig4.show()

#%%
# Remove rows with missing or empty related_same_day_brand
df_church = df_church.filter(pl.col('related_same_day_brand') != '')
df_other_church = df_other_church.filter(pl.col('related_same_day_brand') != '')

# Group by hour and region for both datasets
church_hourly_summary = df_church.group_by(['region', 'hour']).agg(pl.col('visit_count').sum().alias('total_visits'))
other_church_hourly_summary = df_other_church.group_by(['region', 'hour']).agg(pl.col('visit_count').sum().alias('total_visits'))

# Convert to Pandas for visualization
church_hourly_summary_pd = church_hourly_summary.to_pandas()
other_church_hourly_summary_pd = other_church_hourly_summary.to_pandas()

# Visualize hourly usage using scatter plot for other churches for better clarity
fig3 = px.scatter(church_hourly_summary_pd, x='hour', y='total_visits', color='region', title='Hourly Visits: Church of Jesus Christ')
fig4 = px.scatter(other_church_hourly_summary_pd, x='hour', y='total_visits', color='region', title='Hourly Visits: Other Churches')

# Display charts
fig3.show()
fig4.show()

#%%
# Contrast related_same_day_brand brands between those who visit the Church of Jesus Christ of Latter-day Saints and those who visit other churches
church_brands = df_church.group_by('related_same_day_brand').agg(pl.col('related_same_day_brand').count().alias('brand_count')).sort('brand_count', descending=True)
other_church_brands = df_other_church.group_by('related_same_day_brand').agg(pl.col('related_same_day_brand').count().alias('brand_count')).sort('brand_count', descending=True)

# Convert to Pandas for comparison
church_brands_pd = church_brands.to_pandas()
other_church_brands_pd = other_church_brands.to_pandas()

# Visualization
fig5 = px.bar(
    church_brands_pd.head(20),  # Limit to top 20 for better readability
    x='related_same_day_brand',
    y='brand_count',
    title='Top 20 Related Same Day Brands: Church of Jesus Christ Visitors',
    labels={'brand_count': 'Count', 'related_same_day_brand': 'Brand'},
    template='plotly_white'
)
fig5.update_layout(xaxis_tickangle=-45, xaxis_title='Brand', yaxis_title='Count', height=500)

fig6 = px.bar(
    other_church_brands_pd.head(20),  # Limit to top 20 for better readability
    x='related_same_day_brand',
    y='brand_count',
    title='Top 20 Related Same Day Brands: Other Church Visitors',
    labels={'brand_count': 'Count', 'related_same_day_brand': 'Brand'},
    template='plotly_white'
)
fig6.update_layout(xaxis_tickangle=-45, xaxis_title='Brand', yaxis_title='Count', height=500)

# Display charts
fig5.show()
fig6.show()

#%%
# Compare related_same_day_brand of temples, seminary buildings, and meetinghouses of The Church of Jesus Christ of Latter-day Saints
df_temple = df_church.filter(df_church['location_name'].str.contains('Temple'))
df_seminary = df_church.filter(df_church['location_name'].str.contains('Seminary'))
df_meetinghouse = df_church.filter(df_church['location_name'].str.contains('Meetinghouse'))

# Check if data is available for temples, seminaries, and meetinghouses
if df_temple.height > 0:
    # Group by related_same_day_brand for each type of building
    temple_brands = df_temple.group_by('related_same_day_brand').agg(pl.col('related_same_day_brand').count().alias('brand_count')).sort('brand_count', descending=True)
    temple_brands_pd = temple_brands.to_pandas()
    # Visualization
    fig7 = px.bar(temple_brands_pd.head(20), x='related_same_day_brand', y='brand_count', title='Top 20 Related Same Day Brands: Temples', labels={'brand_count': 'Count', 'related_same_day_brand': 'Brand'}, template='plotly_white')
    fig7.update_layout(xaxis_tickangle=-45, xaxis_title='Brand', yaxis_title='Count', height=500)
    fig7.show()
else:
    print("No data available for Temples")

if df_seminary.height > 0:
    seminary_brands = df_seminary.group_by('related_same_day_brand').agg(pl.col('related_same_day_brand').count().alias('brand_count')).sort('brand_count', descending=True)
    seminary_brands_pd = seminary_brands.to_pandas()
    # Visualization
    fig8 = px.bar(seminary_brands_pd.head(20), x='related_same_day_brand', y='brand_count', title='Top 20 Related Same Day Brands: Seminary Buildings', labels={'brand_count': 'Count', 'related_same_day_brand': 'Brand'}, template='plotly_white')
    fig8.update_layout(xaxis_tickangle=-45, xaxis_title='Brand', yaxis_title='Count', height=500)
    fig8.show()
else:
    print("No data available for Seminary Buildings")

if df_meetinghouse.height > 0:
    meetinghouse_brands = df_meetinghouse.group_by('related_same_day_brand').agg(pl.col('related_same_day_brand').count().alias('brand_count')).sort('brand_count', descending=True)
    meetinghouse_brands_pd = meetinghouse_brands.to_pandas()
    # Visualization
    fig9 = px.bar(meetinghouse_brands_pd.head(20), x='related_same_day_brand', y='brand_count', title='Top 20 Related Same Day Brands: Meetinghouses', labels={'brand_count': 'Count', 'related_same_day_brand': 'Brand'}, template='plotly_white')
    fig9.update_layout(xaxis_tickangle=-45, xaxis_title='Brand', yaxis_title='Count', height=500)
    fig9.show()
else:
    print("No data available for Meetinghouses")



# %%
