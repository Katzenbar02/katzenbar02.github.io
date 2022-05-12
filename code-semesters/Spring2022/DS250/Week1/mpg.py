#%% Loading in libraires
import pandas as pd
import altair as alt

# %%Loading in data

mpg =pd.read_csv("mpg.csv")
print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))



# %%
chartleft = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    )
  .transform_loess("displ", "hwy")
  .mark_line())




#%%
chartmiddle = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    detail = "drv"
    )
  .transform_loess("displ", "hwy", groupby = ["drv"])
  .mark_line())

print(chartmiddle)




#%%
chartright = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color=alt.Color("drv", legend=None)
    )
  .transform_loess("displ", "hwy", groupby = ["drv"])
  .mark_line())
#%%
chartleft.save("altair_chartleft.png")
chartmiddle.save("altair_chartmiddle.png")
chartright.save("altair_chartright.png")

# %%
chartp = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy"
  )
  .mark_circle()
)

chart = chartp + chartleft  

chart.save("altair_chartcombine.png")
  

# %%
base =(alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy"
  ))

chart = base.encode(color = "drv").mark_circle() + base.transform_loess("displ", "hwy").mark_line()

chart.save("altair_combine_clean_color.png")
# %%

#column name of class does not work nicely with Altair filter.

base = (alt.Chart(mpg.rename(columns = {"class": "class1"}))
  .encode(
    x = "displ",
    y = "hwy"
    ))

chart_smooth_sub = (base
  .transform_filter(alt.datum.class1 == "subcompact")
  .transform_loess("displ", "hwy")
  .mark_line()
)  

chart = base.encode(color = "class1").mark_circle() + chart_smooth_sub

chart.save("altair_combine_clean_color_filter.png")
# %%





# # %% Making a scatterplot want to color by species
# car_chart = alt.Chart(mpg, title="Setosa seems to have wider Sepals").mark_bar().encode(
#     alt.X("displ", title="`displ`"),
#     alt.Y("hwy", title="hwy")
# ).properties(width=400, height=300)
# car_chart

# # %% Saving altair chart

# alt.Chart(mpg).transform_window(
#     cumulative_count="count()",
#     sort=[{"manufacturer": "year"}],
# ).mark_area().encode(
#     x="IMDB_Rating:Q",
#     y="cumulative_count:Q"
# )
# # car_chart.save("carChart.png")


# #Making a boxplot showing distrution of Sepal Width
# title = "Distribution of Sepal Width"
# iris_chart2 = alt.Chart(mpg,title=title).mark_boxplot(color="dodgerblue").encode(
#     alt.X("species", title="Iris Sepcies"),
#     alt.Y("sepal_width", title="Sepal Width"),
# ).properties(width=400, height=300)

# iris_chart2

# # Saving altair chart
# iris_chart2.save("iris_chart2.svg")
# #%%
# table = mpg.head(5)
# print(table.to_markdown())









