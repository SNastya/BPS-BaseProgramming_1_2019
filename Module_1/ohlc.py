import argparse
import datetime
import sys
import pandas as pd


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=argparse.FileType())
    parser.add_argument('-tf', '--timeframe', type=str)
    parser.add_argument('-t', '--tickets', type=str, nargs='+')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print(namespace)

    text = namespace.name
    numTickets = namespace.numTickets
    timeframe = namespace.timeframe
    tickets = namespace.tickets

    df = pd.read_csv(text, names=['Company', 'Price', 'Amount', 'DateTime'])


df['Dates'] = pd.to_datetime(df['DateTime']).dt.date
df['Time'] = pd.to_datetime(df['DateTime']).dt.time

df = df[(df['Time'] >= datetime.time(7, 0, 0)) & (df['Time'] <= datetime.time(23, 59, 59, 999999)) |
        (df['Time'] >= datetime.time(0, 0, 0)) & (df['Time'] <= datetime.time(2, 59, 59, 999999))]

df['DateTime'] = pd.to_datetime(df['DateTime'])
df = df.set_index('DateTime')
df = df.drop(columns=['Dates', 'Time', 'Amount'])


def trades(df1, timeframe1, tickets1):
    timeframe1 += 'Min'
    data = pd.DataFrame()
    for i in range(len(tickets1)):
        t = tickets1[i]
        tickets1[i] = df1[df1['Company'] == tickets1[i]]
        tickets1[i] = pd.DataFrame(tickets1[i])
        tickets1[i] = tickets1[i]['Price'].resample(timeframe1).ohlc()
        tickets1[i]['Company'] = t
        data = data.append(tickets1[i])
    data = data.query("open != 'NaN'")
    data.sort_values(["DateTime"], inplace=True)
    data = data.reset_index()
    data = data.set_index('Company')
    data = data.reset_index()
    return data.to_csv()


print(trades(df, timeframe, tickets))
