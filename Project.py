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
# print(df1.dtypes)

# # Selecting specific years to print
df3 = df1[(df1['year'] >= 1978) & (df1['year'] <= 1987)]
df4 = df3[[" Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg ", " Switzerland ", " Austria ", " Scandinavia ", " CIS & Eastern Europe "]]
# print(df3)

# # Sorting for Top 3 Countries
ps1 = df4.sum().sort_values(ascending=False)
top3countries = ps1.head(3)
# print(ps1)
# print(top3countries)
top3countries.index

# # Plotting the graph for Top 3 Countries
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=6, rotation=30)
plt.title('Top 3 Europe Countries from 1978 to 1987 (Period:1978-1987)')
plt.bar(top3countries.index, top3countries.values/10000)
plt.show()


# # Plotting for all Europe Region Country
index = np.arange(len(ps1.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps1.index, fontsize=6, rotation=30)
plt.title('Europe Countries from 1978 to 1987 (Period:1978-1987)')
plt.bar(ps1.index,  ps1.values/10000)
plt.show()
