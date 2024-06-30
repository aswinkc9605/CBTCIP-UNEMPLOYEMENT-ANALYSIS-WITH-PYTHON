import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Unemployment.csv")
print(data.head())
data['Date']=pd.to_datetime(data['Date'],format='%d-%m-%Y')
data.dropna(inplace=True)

summary=data.describe(include='all')
print(summary)

missing=data.isnull().sum()
print(missing)

covid_period=data[data['Date']>='2020-03-01']

plt.figure(figsize=(15, 10))
sns.lineplot(data=covid_period, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', legend=None)
plt.title('Unemployment Rate in India (COVID-19 Period)')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.show()

unemployment=covid_period.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
print('Region with lowest unemployment rate')
print(unemployment.head())

print('Region with highest unemployment rate')
print(unemployment.tail())