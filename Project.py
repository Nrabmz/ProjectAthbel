import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('IMVA.xlsx')
df1 = df[["Periods", " Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg ", " Switzerland ", " Austria ", " Scandinavia ", " CIS & Eastern Europe "]]
# print(df1)
df2 = df1['Periods'].str.split(' ', n=2, expand=True)
# print(df2)
df1 = df1.assign(year=df2[1])
df1 = df1.assign(month=df2[2])
print(df1.dtypes)
#print(df1)
df1["year"] = pd.to_numeric(df1["year"])