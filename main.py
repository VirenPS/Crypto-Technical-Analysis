from datetime import datetime

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('2015 to 2021 data open with notepad.txt',
                 sep=";", header=None)

df.columns = ["Date", "Time", "Open", "High", "Low", "Close", "Volume"]


start_date = datetime(2021, 9, 1, 0, 0)
end_date = datetime(2021, 10, 1, 0, 0)

df['DateTime'] = pd.to_datetime(
    df['Date'] + " " + df['Time'], format='%d/%m/%Y %H:%M:%S')

df.to_csv('test2.csv')

mask = (df['DateTime'] > start_date) & (df['DateTime'] <= end_date)
df = df.loc[mask]


# df = df.head(10000)
# condensed_data = df.head()

# print(condensed_data)

# condensed_data['DateTime'] = pd.to_datetime(
#     condensed_data['Date'] + " " + condensed_data['Time'], format='%d/%m/%Y %H:%M:%S')

print('DateTime column created.')

fig = go.Figure(
    data=[
        go.Candlestick(x=df['DateTime'],
                       open=df['Open'],
                       high=df['High'],
                       low=df['Low'],
                       close=df['Close']
                       )
    ]
)


# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

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
