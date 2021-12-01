import pandas as pd
import plotly.figure_factory as px

list1 = pd.read_csv("data.csv")
list = list1["Avg Rating"]

fig = px.create_distplot([list],["Avg Rating"])
fig.show()