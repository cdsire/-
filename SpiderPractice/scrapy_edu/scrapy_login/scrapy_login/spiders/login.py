# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['10.36.131.71']
    start_urls = ['http://10.36.131.71:8888/login/']

    def parse(self, response):
        print(response.body)
        username = "admin"
        password = "qianfeng"
        return FormRequest.from_response(response,formdata={"username":username,"password":password},callback="self.get_content")

    def get_content(self,response):
        print(response.body)

