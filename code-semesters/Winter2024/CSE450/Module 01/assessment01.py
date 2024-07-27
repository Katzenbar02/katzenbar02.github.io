#%%
import pandas as pd

# # Load the dataset into a Pandas data frame
netdf = pd.read_csv('netflix_titles.csv')

# # Determine the data type of the release_year feature
release_year_dtype = netdf['release_year'].dtype
print(release_year_dtype)

# # Filter the dataset to contain only TV Shows
tv_shows = netdf[netdf['type'] == 'TV Show']

# # Count the number of TV Shows rated TV-Y7
tv_y7_count = tv_shows[tv_shows['rating'] == 'TV-Y7'].shape[0]
print(tv_y7_count)

# Filter the dataset to contain only TV Shows released between 2000 and 2009
tv_shows_2000s = tv_shows[(tv_shows['release_year'] >= 2000) & (tv_shows['release_year'] <= 2009)]

# Count the number of TV Shows rated TV-Y7 in the 2000s
tv_y7_count_2000s = tv_shows_2000s[tv_shows_2000s['rating'] == 'TV-Y7'].shape[0]
print(tv_y7_count_2000s)


cerdf = pd.read_csv('cereal.csv')

# Filter the dataset to contain only cereal brands manufactured by Kelloggs
kelloggs_cereal = cerdf[cerdf['mfr'] == 'K']

# Calculate the median amount of protein in Kelloggs cereal brands
median_protein_kelloggs = kelloggs_cereal['protein'].median()

print(median_protein_kelloggs)

# Calculate the healthiness rating for each cereal
cerdf['healthiness'] = (cerdf['protein'] + cerdf['fiber']) / cerdf['sugars']

# Filter the dataset to contain only General Mills cereals
general_mills_cereal = cerdf[cerdf['mfr'] == 'G']

# Calculate the median healthiness value for General Mills cereals
median_healthiness_general_mills = round(general_mills_cereal['healthiness'].median(), 2)

print(median_healthiness_general_mills)


titadf = pd.read_csv('titanic.csv')
print(titadf.head())

# Add a new column called NameGroup containing the first letter of the passenger's surname in lower case
titadf['NameGroup'] = titadf['Name'].str[0].str.lower()

print(titadf['NameGroup'])

# Count the number of passengers with a NameGroup value of 'k'
namegroup_k_count = titadf[titadf['NameGroup'] == 'k'].shape[0]
print(namegroup_k_count)
