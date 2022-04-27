import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846,1303171035, 207847528, 36394523],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja', xlabel='Kontynent', rot=0, legend=True, title='Populacja dla kontynentu', color='red')
# plt.legend(loc='upper left')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', y='Wartość zamówienia', autopct='%.2f %%', fontsize=20, figsize=(6, 6))
# plt.legend(loc='upper left')
# plt.show()
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts)
# print(df)
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# print(df)
# df.plot()
# plt.legend(['Wartości', 'Średnia krocząca'])
# plt.show()

# ZAD 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
grupa = df.groupby('Imie').agg('Rok')
grupa.plot(kind='bar', ylabel='Rok', xlabel='Imie', rot=0, legend=True, title='Imiona i Wiek')

# ZAD 4
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Sprzedawca').agg({'Utarg':['sum']})
# grupa.plot(kind='bar', ylabel='Utarg', xlabel='Sprzedawca', rot=0, legend=True, title='Imiona i Wiek')
# plt.legend(loc='upper left')
# plt.show()