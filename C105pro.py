import csv
from collections import Counter
import pandas as pd
import plotly.express as px

with open('SOCR-HeightWeight.csv') as r:
    read = csv.reader(r)
    data = list(read)

data.pop(0)
m =len(data)
t =0

for x in data:
    t=t+float(x[1])

mean = t/m
print(mean)


df= pd.read_csv('SOCR-HeightWeight.csv')
fig = px.scatter(df,x='Height(Inches)', y ='Weight(Pounds)')
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=mean, y1=mean,
        x0=0 , x1=m,

    )
])
fig .update_yaxes(rangemode='tozero')

fig.show()

