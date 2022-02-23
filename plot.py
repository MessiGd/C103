import pandas as pd
import plotly.express as px

a = pd.read_csv("data2.csv")
fig = px.line(a , x = "Country", y = "Per capita income", color = "Year", title = "Per Capita income of countries")
fig.show()
