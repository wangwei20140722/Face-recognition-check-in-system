from aip import AipSpeech
import os
import time


def baidu_voice(voice):
    """ 你的 APPID AK SK """
    APP_ID = '**'
    API_KEY = '***'
    SECRET_KEY = '***'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(voice, 'zh', 1, {
        'vol': 8,'per':0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    #time.sleep(4)
    os.system('auido.mp3')

    #time.sleep(t)
#baidu_voice('欢迎来到郑州轻工业大学ai人工智能实验室')
#baidu_voice('欢迎张文豪进入实验室')
#baidu_voice('欢迎张文豪进入实验室')
