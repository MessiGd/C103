import pandas as pd
import plotly.express as px

a = pd.read_csv("data.csv")
fig = px.scatter(a, x = "Country", y = "Percentage", color= "InternetUsers", size = "Population", size_max = 60)
fig.show()