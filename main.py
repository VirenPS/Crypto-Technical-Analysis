from datetime import datetime

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('2015 to 2021 data open with notepad.txt',
                 sep=";", header=None)

df.columns = ["Date", "Time", "Open", "High", "Low", "Close", "Volume"]

df = df.head()
# condensed_data = df.head()

# print(condensed_data)

# condensed_data['DateTime'] = pd.to_datetime(
#     condensed_data['Date'] + " " + condensed_data['Time'], format='%d/%m/%Y %H:%M:%S')
df['DateTime'] = pd.to_datetime(
    df['Date'] + " " + df['Time'], format='%d/%m/%Y %H:%M:%S')


fig = go.Figure(data=[go.Candlestick(x=df['DateTime'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.update_xaxes(
    rangeslider_visible=True,
    tickformatstops=[
        dict(dtickrange=[60000, 3600000], value="%H:%M m"),
        dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
        dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
        dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
        dict(dtickrange=["M1", "M12"], value="%b '%y M"),
        dict(dtickrange=["M12", None], value="%Y Y")
    ]
)

fig.show()
