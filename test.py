import MetaTrader5 as mt5
import os
from os.path import join, dirname
from dotenv import load_dotenv

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
 
# MetaTrader 5ターミナルへの接続をシャットダウンする
mt5.shutdown()