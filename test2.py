from datetime import datetime

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('2015 to 2021 data open with notepad.txt',
                 sep=";", header=None)

df.columns = ["Date", "Time", "Open", "High", "Low", "Close", "Volume"]

print(df.head())

dates = df["Date"].unique()

# for i in dates:
#     print(i)
