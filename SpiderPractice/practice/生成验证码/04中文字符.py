# -*- coding: utf-8 -*-
import random


class RandomChar():
    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x9FBF)    # 汉字的Unicode编码范围
        return unichr(val)

    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)  # 汉字的gb2312编码范围
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = (head << 8) | (body << 4) | tail
        str = "%x" % val
        return str.decode('hex').decode('gb2312')

for i in range(4):
    print RandomChar.GB2312()
    print type(RandomChar.GB2312())

