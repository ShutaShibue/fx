import MetaTrader5 as mt5
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import mplfinance as mpf


register_matplotlib_converters()
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# MetaTrader 5パッケージについてのデータを表示する
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 

id = int(os.environ.get("ID"))
Pass = os.environ.get('Pass')
if not mt5.initialize(login=id, server="OANDA-Japan MT5 Live", password=Pass):
   print("initialize() failed, error code =",mt5.last_error())
   quit()

# 接続状態、サーバ名、取引口座に関するデータを表示する
print(mt5.terminal_info())
# MetaTrader 5バージョンについてのデータを表示する
print(mt5.version())
 
rates = mt5.copy_rates_from("USDJPY", mt5.TIMEFRAME_D1, datetime(2022,8,5), 200)
mt5.shutdown()

df = pd.DataFrame(rates)
df['time']=pd.to_datetime(df['time'], unit='s')

df.set_index('time', inplace = True)
mpf.plot(df, type='candle', style="yahoo")
