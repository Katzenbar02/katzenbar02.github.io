#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import catboost as cb
from sklearn import metrics

"""Grand Questions 1
Create 2-3 charts that evaluate potential relationships between the home variables and before1980. Explain what you learn from the charts that could help a machine learning algorithm.
Build a classification model labeling houses as being built “before 1980” or “during or after 1980”. Your goal is to reach or exceed 90% accuracy. Explain your final model choice (algorithm, tuning parameters, etc) and describe what other models you tried.
Justify your classification model by discussing the most important features selected by your model. This discussion should include a chart and a description of the features.
Describe the quality of your classification model using 2-3 different evaluation metrics. You also need to explain how to interpret each of the evaluation metrics you use.
"""
#%%
# import data
alt.data_transformers.disable_max_rows()

dwellings_denver = 'dwellings_denver.csv'
dwellings_ml = 'dwellings_ml.csv'
dwellings_neighborhoods_ml = 'dwellings_neighborhoods_ml.csv'

dwellings_denver = pd.read_csv(dwellings_denver)
dwellings_ml = pd.read_csv(dwellings_ml)
dwellings_neighborhoods_ml = pd.read_csv(dwellings_neighborhoods_ml)

#%%
dwellings_ml.columns


# %%Aggregate data and create the dwellings_table
dwellings_table = (
    dwellings_ml.groupby('yrbuilt')
    .agg(
        sprice_avg=('sprice', np.average),
        stories_avg=('stories', np.average),
        nocars_avg=('nocars', np.average),
        livearea_avg=('livearea', np.average),
        numbdrm_avg=('numbdrm', np.average),
        numbaths_avg=('numbaths', np.average)
    )
    .reset_index()
)

#%% Filter and select desired columns
dwellings_table = dwellings_table[['yrbuilt', 'sprice_avg', 'stories_avg', 'nocars_avg', 'livearea_avg', 'numbdrm_avg', 'numbaths_avg']]

#%% Create an overlay chart to mark 1980
overlay = (
    alt.Chart(dwellings_table.query("yrbuilt == 1980"))
    .mark_rule(color='red')
    .encode(x='yrbuilt')
)

# %%Create the main area chart
chart1 = (
    alt.Chart(dwellings_table)
    .mark_area()
    .encode(
        x=alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
        y=alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
    )
    .properties(
        title={
            "text": "Average Selling Price of Houses by Year",
        }
    )
)

#%% Overlay the charts to create the final chart
final_chart1 = (chart1 + overlay).configure_title(
    fontSize=15,
    anchor="start",
    subtitleFontSize=11
)

#%% Display the charts
chart1
#%%
final_chart1





#%% Aggregate data and create the dwellings_table
dwellings_table = (
    dwellings_ml.groupby('yrbuilt')
    .agg(
        sprice_avg=('sprice', np.average),
        stories_avg=('stories', np.average),
        nocars_avg=('nocars', np.average),
        livearea_avg=('livearea', np.average),
        numbdrm_avg=('numbdrm', np.average),
        numbaths_avg=('numbaths', np.average)
    )
    .reset_index()
)

#%% Filter and select desired columns
dwellings_table = dwellings_table[['yrbuilt', 'sprice_avg', 'stories_avg', 'nocars_avg', 'livearea_avg', 'numbdrm_avg', 'numbaths_avg']]

#%% Create an overlay chart to mark 1980
overlay = (
    alt.Chart(dwellings_table.query("yrbuilt == 1980"))
    .mark_rule(color='red')
    .encode(x='yrbuilt')
)

#%% Create a function to generate the final chart with overlay
def create_final_chart(chart, title):
    final_chart = (alt.layer(chart, overlay)
        .configure_title(
            fontSize=15,
            anchor="start",
            subtitleFontSize=11
        )
    )
    final_chart.title = title
    return final_chart

#%% Create multiple charts with overlays
chart1 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
)

chart2 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('stories_avg', axis=alt.Axis(title="Average Number of Stories"))
)

chart3 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('nocars_avg', axis=alt.Axis(title="Average Number of Cars in Garage"))
)

chart4 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('livearea_avg', axis=alt.Axis(title="Average Living Area"))
)

chart5 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('numbdrm_avg', axis=alt.Axis(title="Average Number of Bedrooms"))
)

chart6 = alt.Chart(dwellings_table).mark_bar().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('numbaths_avg', axis=alt.Axis(title="Average Number of Bathrooms"))
)


#%% Generate final charts with overlays
final_chart1 = create_final_chart(chart1, "Average Selling Price of Houses by Year")
final_chart2 = create_final_chart(chart2, "Average Number of Stories in Houses by Year")
final_chart3 = create_final_chart(chart3, "Average Number of Cars in Garage by Year")
final_chart4 = create_final_chart(chart4, "Average Living Area in Houses by Year")
final_chart5 = create_final_chart(chart5, "Average Number of Bedrooms in Houses by Year")
final_chart6 = create_final_chart(chart6, "Average Number of Bathrooms in Houses by Year")

#%% Display the final charts
final_chart1
#%%
final_chart2
#%%
final_chart3
#%%
final_chart4
#%%
final_chart5
#%%
final_chart6








#%%
dwellings_ml.describe()

'''
CLASSIFICATION MODEL 1 (GaussianNB)
'''

#%% Prepare the features and targets numpy arrays
features = dwellings_ml[['yrbuilt']].to_numpy()
targets = dwellings_ml[['before1980']].to_numpy()

# Split the data into training and testing variables
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42, stratify=targets)

# Fit the GaussianNB classifier model
classifier = GaussianNB()
classifier.fit(features_train, targets_train.ravel())

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(predictions, targets_test)
print(f"Model 1 (GaussianNB) Accuracy: {accuracy}")

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(targets_test, predictions))
print()

'''
CLASSIFICATION MODEL 2 (RandomForestClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
targets = dwellings_ml[['before1980']].to_numpy()

# Split the data into training and testing variables
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=24)

# Fit the RandomForestClassifier model
classifier = RandomForestClassifier(random_state=24)
classifier.fit(features_train, targets_train.ravel())

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(predictions, targets_test)
print(f"Model 2 (RandomForestClassifier) Accuracy: {accuracy}")

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(targets_test, predictions))
print()

'''
CLASSIFICATION MODEL 3 (DecisionTreeClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']]
targets = dwellings_ml[['before1980']]

# Split the data into training and testing variables
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)

# Fit the DecisionTreeClassifier model
classifier = DecisionTreeClassifier()
classifier.fit(features_train, targets_train)

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(predictions, targets_test)
print(f"Model 3 (DecisionTreeClassifier) Accuracy: {accuracy}")

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(targets_test, predictions))
print()

'''
CLASSIFICATION MODEL 4 (GradientBoostingClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
targets = dwellings_ml[['before1980']].to_numpy()

# Split the data into training and testing variables
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)

# Fit the GradientBoostingClassifier model
classifier = GradientBoostingClassifier(random_state=42)
classifier.fit(features_train, targets_train.ravel())

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(predictions, targets_test)
print(f"Model 4 (GradientBoostingClassifier) Accuracy: {accuracy}")

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(targets_test, predictions))
print()

'''
CLASSIFICATION MODEL 5 (CatBoostClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
targets = dwellings_ml[['before1980']].to_numpy()

# Split the data into training and testing variables
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)

# Fit the CatBoostClassifier model
classifier = cb.CatBoostClassifier(iterations=10, depth=6, learning_rate=1, loss_function='Logloss', verbose=False)
classifier.fit(features_train, targets_train)

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(predictions, targets_test)
print(f"Model 5 (CatBoostClassifier) Accuracy: {accuracy}")

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(targets_test, predictions))
print()
























# #%%
# # create a table for the charts
# dwellings_table = (dwellings_ml
#     .groupby('yrbuilt')
#         .agg(
#             sprice_avg = ('sprice', np.average),
#             stories_avg = ('stories', np.average),
#             nocars_avg = ('nocars', np.average),
#             livearea_avg = ('livearea', np.average),
#             numbdrm_avg = ('numbdrm', np.average),
#             numbaths_avg = ('numbaths', np.average)
#         )
#         .filter(
#             ['yrbuilt', 'sprice_avg', 'stories_avg', 'nocars_avg', 'livearea_avg', 'numbdrm_avg', 'numbaths_avg']
#         )
#         .reset_index()
#     )

# dwellings_table

# #%%
# # create an overlay chart to mark 1980
# overlay = (alt.Chart(dwellings_table.query("yrbuilt == 1980"))
#     .encode(
#         # variables go here
#             x = 'yrbuilt'
#             # variables for .mark_point()
#             #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
#             #color = 'name'
#         )
#     # attributes go here
#     .mark_rule(color = 'red')
# )

# #%%
# chart1 = alt.Chart(dwellings_table).mark_area().encode(
#     alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
#     alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
# ).properties(
#     title = {
#         "text":"Average Selling Price of a House each Year",
#     }
# )

# # overlay the charts to create a better chart
# final_chart1 = (alt.layer(chart1, overlay)
#     .configure_title(
#         fontSize = 15,
#         anchor = "start",
#         subtitleFontSize = 11
#     )
# )
# chart1
# final_chart1

# # %%

# %%
