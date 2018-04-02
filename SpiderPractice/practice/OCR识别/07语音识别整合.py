# -*- coding: utf-8 -*-
'''
1.下面的类recoder是一个录音类，专门用来识别录制音频

'''
import numpy as np
import wave
import os

from pyaudio import PyAudio,paInt16
from datetime import datetime
from aip import AipSpeech


# 录音
class recoder:
    NUM_SAMPLES = 2000  # pyaudio内置缓冲大小
    SAMPLING_RATE = 8000  # 取样频率
    LEVEL = 500  # 声音保存的阈值
    COUNT_NUM = 20  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
    SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
    TIME_COUNT = 60  # 录音时间，单位s

    Voice_String = []

    def savewav(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.SAMPLING_RATE)
        wf.writeframes(np.array(self.Voice_String).tostring())
        # wf.writeframes(self.Voice_String.decode())
        wf.close()

    def recoder(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        save_count = 0
        save_buffer = []
        time_count = self.TIME_COUNT

        while True:
            time_count -= 1
            # print time_count
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(self.NUM_SAMPLES)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum(audio_data > self.LEVEL)
            print(np.max(audio_data))
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.COUNT_NUM:
                save_count = self.SAVE_LENGTH
            else:
                save_count -= 1

            if save_count < 0:
                save_count = 0

            if save_count > 0:
                # 将要保存的数据存放到save_buffer中
                # print  save_count > 0 and time_count >0
                save_buffer.append(string_audio_data)
            else:
                # print save_buffer
                # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
                # print "debug"
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
            if time_count == 0:
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False

# 读取文件
def get_file_content(filePath):
    with open(filePath,"rb") as fp:
        return fp.read()


if __name__ == '__main__':
    APP_ID = "10994778"
    API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
    SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    while True:
        r = recoder()
        r.recoder()
        r.savewav("1.wav")
        # 识别本地文件
        result = client.asr(get_file_content('1.wav'),'wav',8000,{
            'lan':'zh',
        })
        print result['result'][0]
        if u"记事本," == result["result"][0]:
            os.system("notepad")
        elif u"计算器," == result['result'][0]:
            os.system("calc")
        elif u"关机," == result["result"][0]:
            os.system("shutdown -s -t 300")
        elif u"取消关机," == result['result'][0]:
            os.system("shutdown -a")
        else:
            pass
