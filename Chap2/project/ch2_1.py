"""
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""


import json, requests
from sys import exit

KEY = '4e26a0b843754c17a4b03f9acdd692a5'
API = 'https://free-api.heweather.com/v5/now'


history = [] #存放历史数据

def get_weather_info(query):
    payload = {'key':KEY, 'city':query}
#    r = requests.get(API, params = payload)
    r = requests.get(f"https://free-api.heweather.com/v5/now?city={query}&key={KEY}")
    return r.json()

def show_weather_info(result):
    dict_basic = result['HeWeather5'][0]['basic']
    dict_now = result['HeWeather5'][0]['now']

    weather_info = dict_now['cond']['txt']
    weather_temp = dict_now['tmp']
    weather_wind = dict_now['wind']['dir']
    weather_city = dict_basic['city']
    weather_update = dict_basic['update']['loc']

    print(f"{weather_city}的天气状况{weather_info}，风向{weather_wind},温度{weather_temp},最后更新时间{weather_update}")

    history.append([query, weather_update])

def get_help():
    print("---------------------------")
    print("输入城市名，查询该城市的天气；")
    print("输入help，获取帮助文档；")
    print("输入history，获取查询历史；")
    print("输入quit，退出天气查询系统。")

def get_history():
    print(f"查询的历史数据为：{history}")



while True:
    print("请输入指令或城市名")
    query = input(">")

    if query == 'h' or query == 'help':
        get_help()

    elif query == 'exit' or query == 'quit':
        exit(0)

    elif query == 'history':
        get_history()

    else:
        try:
            result = get_weather_info(query)
            show_weather_info(result)
        except:
            print("请重新输入")
            continue
