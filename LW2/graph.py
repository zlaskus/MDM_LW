import pandas as pd
from plotly import graph_objects as go

data = pd.read_csv('NetTraffic.csv')

time = list(set(data['Time']))
time.sort()
rate = list()
for i in range(len(time)):
    rate.append(data['Rate(MB)'].loc[data['Time'] == time[i]].sum())

fig = go.Figure(data=go.Scatter(x=time, y=rate, mode='lines+markers'))
fig.write_html('graph.html')