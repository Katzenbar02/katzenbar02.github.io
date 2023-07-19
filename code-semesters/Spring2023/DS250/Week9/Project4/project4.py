#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import catboost as cb
from sklearn import metrics

#%%
# import data
alt.data_transformers.disable_max_rows()

dwellings_denver = 'dwellings_denver.csv'
dwellings_ml = 'dwellings_ml.csv'
dwellings_neighborhoods_ml = 'dwellings_neighborhoods_ml.csv'

dwellings_denver = pd.read_csv(dwellings_denver)
dwellings_ml = pd.read_csv(dwellings_ml)
dwellings_neighborhoods_ml = pd.read_csv(dwellings_neighborhoods_ml)




# GRAND QUESTION 1

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
# chart1 = alt.Chart(dwellings_table).mark_bar().encode(
#     alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
#     alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
# )

# chart2 = alt.Chart(dwellings_table).mark_bar().encode(
#     alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
#     alt.Y('stories_avg', axis=alt.Axis(title="Average Number of Stories"))
# )

# chart3 = alt.Chart(dwellings_table).mark_bar().encode(
#     alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
#     alt.Y('nocars_avg', axis=alt.Axis(title="Average Number of Cars in Garage"))
# )

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
# final_chart1 = create_final_chart(chart1, "Average Selling Price of Houses by Year")
# final_chart2 = create_final_chart(chart2, "Average Number of Stories in Houses by Year")
# final_chart3 = create_final_chart(chart3, "Average Number of Cars in Garage by Year")
final_chart4 = create_final_chart(chart4, "Average Living Area in Houses by Year")
final_chart5 = create_final_chart(chart5, "Average Number of Bedrooms in Houses by Year")
final_chart6 = create_final_chart(chart6, "Average Number of Bathrooms in Houses by Year")

# #%% Display the final charts
# final_chart1
# #%%
# final_chart2
# #%%
# final_chart3
#%%
final_chart4
#%%
final_chart5
#%%
final_chart6





# GRAND QUESTION 2

'''
CLASSIFICATION MODEL 1 (GaussianNB)
'''

#%% Prepare the features and targets numpy arrays
features = dwellings_ml[['yrbuilt']].to_numpy()
targets = dwellings_ml[['before1980']].to_numpy()

# Split the data into training and testing variables with stratified split
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42, stratify=targets)

# Classification Model 1 (GaussianNB)
classifier1 = GaussianNB()
classifier1.fit(features_train, targets_train.ravel())
predictions1 = classifier1.predict(features_test)
accuracy1 = metrics.accuracy_score(predictions1, targets_test)
print(f"Model 1 (GaussianNB) Accuracy: {accuracy1:.3f}")

'''
CLASSIFICATION MODEL 2 (RandomForestClassifier)
'''

features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)
classifier2 = RandomForestClassifier(random_state=42)
classifier2.fit(features_train, targets_train.ravel())
predictions2 = classifier2.predict(features_test)
accuracy2 = metrics.accuracy_score(predictions2, targets_test)
print(f"Model 2 (RandomForestClassifier) Accuracy: {accuracy2:.3f}")

'''
CLASSIFICATION MODEL 3 (DecisionTreeClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)
classifier3 = DecisionTreeClassifier()
classifier3.fit(features_train, targets_train)
predictions3 = classifier3.predict(features_test)
accuracy3 = metrics.accuracy_score(predictions3, targets_test)
print(f"Model 3 (DecisionTreeClassifier) Accuracy: {accuracy3}")

'''
CLASSIFICATION MODEL 4 (GradientBoostingClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)
classifier4 = GradientBoostingClassifier(random_state=42)
classifier4.fit(features_train, targets_train.ravel())
predictions4 = classifier4.predict(features_test)
accuracy4 = metrics.accuracy_score(predictions4, targets_test)
print(f"Model 4 (GradientBoostingClassifier) Accuracy: {accuracy4}")


'''
CLASSIFICATION MODEL 5 (CatBoostClassifier)
'''

# Prepare the features and targets numpy arrays
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths', 'numbdrm', 'totunits', 'arcstyle_SPLIT LEVEL']].to_numpy()
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42)
classifier5 = cb.CatBoostClassifier(iterations=10, depth=6, learning_rate=1, loss_function='Logloss', verbose=False)
classifier5.fit(features_train, targets_train)
predictions5 = classifier5.predict(features_test)
accuracy5 = metrics.accuracy_score(predictions5, targets_test)
print(f"Model 5 (CatBoostClassifier) Accuracy: {accuracy5}")






# grand question 3

#%%
features = dwellings_ml[['sprice', 'stories', 'nocars', 'livearea', 'basement', 'numbaths',
                         'numbdrm', 'arcstyle_END UNIT', 'arcstyle_MIDDLE UNIT',
                         'arcstyle_ONE AND HALF-STORY', 'arcstyle_ONE-STORY', 'arcstyle_TWO-STORY',
                         'status_I', 'gartype_Det', 'gartype_Att', 'quality_C', 'quality_B',
                         'condition_Good', 'condition_AVG', 'deduct', 'totunits', 'finbsmnt', 'abstrprd']]

targets = dwellings_ml['before1980']

# Split the data into training and testing variables with stratified split
features_train, features_test, targets_train, targets_test = train_test_split(features, targets, test_size=0.3, random_state=42, stratify=targets)

# Train the RandomForestClassifier model
classifier = RandomForestClassifier(random_state=42)
classifier.fit(features_train, targets_train)

# Make predictions on the test features
predictions = classifier.predict(features_test)

# Additional Evaluation Metrics
precision = metrics.precision_score(targets_test, predictions)
recall = metrics.recall_score(targets_test, predictions)
f1_score = metrics.f1_score(targets_test, predictions)
roc_auc = metrics.roc_auc_score(targets_test, predictions)

print(f"Model 2 (RandomForestClassifier) Precision: {precision:.3f}")
print(f"Model 2 (RandomForestClassifier) Recall: {recall:.3f}")
print(f"Model 2 (RandomForestClassifier) F1-Score: {f1_score:.3f}")
print(f"Model 2 (RandomForestClassifier) ROC-AUC: {roc_auc:.3f}")

# Plot feature importance with better formatting
feature_df = pd.DataFrame({'features': features.columns, 'importance': classifier.feature_importances_})
feature_chart = alt.Chart(feature_df).mark_bar().encode(
    x='importance',
    y=alt.Y('features', sort='-x'),  # Sort features by importance
    tooltip=['features', 'importance']  # Show tooltip with feature names and importance
).properties(title="Feature Importance of RandomForestClassifier")

# Display the feature importance chart
feature_chart






#%% GRAND QUESTION 4

accuracy = metrics.accuracy_score(predictions2, targets_test)
confusion_matrix = metrics.confusion_matrix(targets_test, predictions2)
classification_report = metrics.classification_report(targets_test, predictions2)

print(f"Accuracy: {accuracy:.3f}")
print("Confusion Matrix:")
print(confusion_matrix)
print("Classification Report:")
print(classification_report)

# Visualize the confusion matrix
plt.figure(figsize=(5, 5))
plt.imshow(confusion_matrix, cmap='Blues', interpolation='nearest')
plt.colorbar()
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['before1980 = 0', 'before1980 = 1'], rotation=45)
plt.yticks(tick_marks, ['before1980 = 0', 'before1980 = 1'])
plt.tight_layout()
plt.show()

# %%
