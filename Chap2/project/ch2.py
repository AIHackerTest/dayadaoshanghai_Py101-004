"""
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""

import requests, json
from sys import exit

KEY = 'uank9lfdtsytasqn' # API key
API = 'https://api.seniverse.com/v3/weather/now.json' #API URL
UNIT = 'c' #单位
LANGUAGE = 'zh-Hans'


# create a list for storing history data
history = []

def get_weather_info(location):
    payload = {'key':KEY, 'location':location, 'language':LANGUAGE, 'unit':UNIT}
    r = requests.get(API, params = payload)
    return r.json()


def show_weather_info(result):
    dict_location = result['results'][0]['location']['name'] #取城市名
    dict_now_weather = result['results'][0]['now']['text'] #取天气状况
    dict_now_temp = result['results'][0]['now']['temperature'] # 取温度状况
    dict_now_code = result['results'][0]['now']['code']
    last_update = result['results'][0]['last_update'] #取更新时间

    print(f"{dict_location}的天气状况为：{dict_now_weather}，气温为{dict_now_temp}摄氏度，最后更新时间为{last_update},天气现象代码为{dict_now_code}")

    history.append([query,dict_now_weather])

    return history

def get_help():
    print("---------------------------")
    print("输入城市名，查询该城市的天气；")
    print("输入help，获取帮助文档；")
    print("输入history，获取查询历史；")
    print("输入quit，退出天气查询系统。")

def get_history():
    print(f"查询的历史记录为：{history}")


while True:
    query = input("请输入指令或您要查询的城市名城市名：")

    if query == 'help' or query == 'h':
        get_help()

    elif query == 'quit' or query == 'exit':
        exit(0)

    elif query == "history":
        get_history()

    else:
        try:
            result = get_weather_info(query)
            show_weather_info(result)
        except:
            print("请重新输入！")
            continue
