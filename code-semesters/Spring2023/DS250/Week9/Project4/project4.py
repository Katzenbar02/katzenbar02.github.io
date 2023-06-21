#%%
# import packages
import pandas as pd
import numpy as np
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""Grand Questions
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


#%%
# create a table for the charts
dwellings_table = (dwellings_ml
    .groupby('yrbuilt')
        .agg(
            sprice_avg = ('sprice', np.average),
            stories_avg = ('stories', np.average),
            nocars_avg = ('nocars', np.average),
            livearea_avg = ('livearea', np.average),
            numbdrm_avg = ('numbdrm', np.average),
            numbaths_avg = ('numbaths', np.average)
        )
        .filter(
            ['yrbuilt', 'sprice_avg', 'stories_avg', 'nocars_avg', 'livearea_avg', 'numbdrm_avg', 'numbaths_avg']
        )
        .reset_index()
    )

dwellings_table

#%%
# create an overlay chart to mark 1980
overlay = (alt.Chart(dwellings_table.query("yrbuilt == 1980"))
    .encode(
        # variables go here
            x = 'yrbuilt'
            # variables for .mark_point()
            #shape = 'year:N' # N = Nominal, O = Ordinal, (year is a variable)
            #color = 'name'
        )
    # attributes go here
    .mark_rule(color = 'red')
)

#%%
chart1 = alt.Chart(dwellings_table).mark_area().encode(
    alt.X('yrbuilt', axis=alt.Axis(title="Year Built")),
    alt.Y('sprice_avg', axis=alt.Axis(title="Average Selling Price"))
).properties(
    title = {
        "text":"Average Selling Price of a House each Year",
    }
)

# overlay the charts to create a better chart
final_chart1 = (alt.layer(chart1, overlay)
    .configure_title(
        fontSize = 15,
        anchor = "start",
        subtitleFontSize = 11
    )
)
chart1
final_chart1
#%%
final_chart1.save("Images/AvgSellingPriceEachYear.png")
# %%
