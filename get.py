import requests


def get(word):
    try:
        url = 'https://fanyi.baidu.com/sug'
        data = {'kw': word}  # 你只需要改kw对应的值
        res = requests.post(url, data=data).json()
        return res['data'][0]['v']
    except:
        return 'None'

