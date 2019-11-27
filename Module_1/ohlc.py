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


def trades_5(df1):
    print( '5MIN DATA' )
    num_tickets = int(input('Input number of tickets: '))
    data = pd.DataFrame()
    for i in range(num_tickets):
        ticket = input('Input name of Tickets: ')
        t = ticket
        ticket = df1[df1['Company'] == ticket]
        ticket = ticket['Price'].resample('5Min').ohlc()
        ticket['Company'] = t
        data = data.append(ticket)
    data = data.query("open != 'NaN'")
    data.sort_values(["DateTime"], inplace=True)
    data = data.reset_index()
    data = data.set_index('Company')
    data = data.reset_index()
    return data

def trades_30(df1):
    print( '30MIN DATA' )
    num_tickets = int(input('Input number of tickets: '))
    data = pd.DataFrame()
    for i in range(num_tickets):
        ticket = input('Input name of Tickets: ')
        t = ticket
        ticket = df1[df1['Company'] == ticket]
        ticket = ticket['Price'].resample('30Min').ohlc()
        ticket['Company'] = t
        data = data.append(ticket)
    data = data.query("open != 'NaN'")
    data.sort_values(["DateTime"], inplace=True)
    data = data.reset_index()
    data = data.set_index('Company')
    data = data.reset_index()
    return data

def trades_240(df1):
    print( '240MIN DATA' )
    num_tickets = int(input('Input number of tickets: '))
    data = pd.DataFrame()
    for i in range(num_tickets):
        ticket = input('Input name of Tickets: ')
        t = ticket
        ticket = df1[df1['Company'] == ticket]
        ticket = ticket['Price'].resample('240Min').ohlc()
        ticket['Company'] = t
        data = data.append(ticket)
    data = data.query("open != 'NaN'")
    data.sort_values(["DateTime"], inplace=True)
    data = data.reset_index()
    data = data.set_index('Company')
    data = data.reset_index()
    return data

print(trades_5(df))
print(trades_30( df))
print(trades_240(df))