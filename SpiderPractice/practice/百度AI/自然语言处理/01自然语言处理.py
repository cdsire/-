# -*- coding: utf-8 -*-
'''
AipNlp是自然语言处理的Python SDK客户端，为使用自然语言处理的开发人员提供了一系列的交互方法。
'''
from aip import AipNlp

APP_ID = "10994778"
API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "百度是一家高科技公司"

# 调用词法分析,lexer:词法分析程序
result = client.lexer(text)
for key in result:
    print key,result[key]

# 调用词法分析（定制版）
result = client.wordEmbedding("百度")
print result

# 词语相似度
result = client.wordSimEmbedding("百度","百科")
print result

# 正负值评价
result = client.sentimentClassify("百度是一家强大的科技公司")
print result

# 返回参数详情
result = client.dnnlm("百度是一家强大的科技公司")
print result

# 带参数调用短文本相似度
result = client.simnet("百度是一家强大的科技公司","强大的百度")
print result

# 评论观点提取，分析情感
result = client.commentTag("百度是一家强大的科技公司")
print result

