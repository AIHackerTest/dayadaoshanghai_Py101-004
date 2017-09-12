# -*- coding: utf-8 -*-
# sript, soure_file = argv

# create a whether dict
whether = {}
his = []
history = {}
# str key

# open whether source file
with open('whe_source.txt', 'rb') as f:
#    f = f.read().decode('utf-8')    为什么这样decode不行？
    for line in f:
        key1, value = line.split(b',')
        key1 = key1.decode('utf-8')
        value = value.decode('utf-8')
        whether[key1] = value


# help
def help_prog():
    print("输入城市名，查询该城市的天气；")
    print("输入help，获取帮助文档；")
    print("输入history，获取查询历史；")
    print("输入quit，退出天气查询系统。")

# histrory function
def his_prog(key):
    print(f"{his}")

def get_weather_info(key):
    try:
        print(f"{key}的天气状况为{whether[key]}")
        his.append(key)
#        histroy[city] = whether[key]
    except:
        print("找不到指令或城市名，请重新输入")
        help_prog()

while True:
    key = input("请输入指令或您需要的城市名：")
    if key == "quit":
        exit(0)

    elif key == "help":
        help_prog()

    elif key == "history":
        his_prog(key)

    else:
        get_weather_info(key)
