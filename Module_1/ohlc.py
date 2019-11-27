import datetime
import pandas as pd

pd.options.display.max_rows = 1500000

df = pd.read_csv('trades.txt', names=['Company', 'Price', 'Amount', 'DateTime'])

df['Dates'] = pd.to_datetime(df['DateTime']).dt.date
df['Time'] = pd.to_datetime(df['DateTime']).dt.time


df = df[(df['Time'] >= datetime.time(7,0,0) ) & (df['Time'] <= datetime.time(23,59,59,999999)) |
        (df['Time'] >= datetime.time(0,0,0) ) & (df['Time'] <= datetime.time(2,59,59,999999) )]


df['DateTime'] = pd.to_datetime(df['DateTime'])

df = df.set_index('DateTime')
df = df.drop(columns= ['Dates','Time', 'Amount'])


sber_df = df[df['Company'] == 'SBER']
aapl_df = df[df['Company'] == 'AAPL']
amzn_df = df[df['Company'] == 'AMZN']



sber_df_5 = sber_df['Price'].resample('5Min').ohlc()
aapl_df_5 = aapl_df['Price'].resample('5Min').ohlc()
amzn_df_5 = amzn_df['Price'].resample('5Min').ohlc()

sber_df_30 = sber_df['Price'].resample('30Min').ohlc()
aapl_df_30 = aapl_df['Price'].resample('30Min').ohlc()
amzn_df_30 = amzn_df['Price'].resample('30Min').ohlc()

sber_df_240 = sber_df['Price'].resample('240Min').ohlc()
aapl_df_240 = aapl_df['Price'].resample('240Min').ohlc()
amzn_df_240 = amzn_df['Price'].resample('240Min').ohlc()





sber_df_5['Company'] = 'SBER'
aapl_df_5['Company'] = 'AAPl'
amzn_df_5['Company'] = 'AMZN'

sber_df_30['Company'] = 'SBER'
aapl_df_30['Company'] = 'AAPl'
amzn_df_30['Company'] = 'AMZN'

sber_df_240['Company'] = 'SBER'
aapl_df_240['Company'] = 'AAPl'
amzn_df_240['Company'] = 'AMZN'


data_5 = aapl_df_5.append(amzn_df_5)
data_5 = data_5.append(sber_df_5)

data_30 = aapl_df_30.append(amzn_df_30)
data_30 = data_30.append(sber_df_30)

data_240 = aapl_df_240.append(amzn_df_240)
data_240 = data_240.append(sber_df_240)


data_5 = data_5.query("low != 'NaN'")
data_5.sort_values(["DateTime"], inplace=True)
data_5 = data_5.reset_index()
data_5 = data_5.set_index('Company')
data_5 = data_5.reset_index()

data_30 = data_30.query("low != 'NaN'")
data_30.sort_values(["DateTime"], inplace=True)
data_30 = data_30.reset_index()
data_30 = data_30.set_index('Company')
data_30 = data_30.reset_index()

data_240 = data_240.query("low != 'NaN'")
data_240.sort_values(["DateTime"], inplace=True)
data_240 = data_240.reset_index()
data_240 = data_240.set_index('Company')
data_240 = data_240.reset_index()

data_5.to_csv
data_30.to_csv
data_240.to_csv


