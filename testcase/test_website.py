import unittest
import sys
import requests
from pubilc import function
import os
import time

class LoginTest(unittest.TestCase):
    '''myapps网站登录测试'''

    def setUp(self):
        pass


    def test_official_website_login(self):
        '''官网登陆测试'''
        title = '天翎官网'
        url = "http://www.teemlink.com"
        r = requests.get(url=url)
        code = r.status_code
        if(code!=200):
            function.send_mail(title)

    def test_experience_website_login(self):
        '''体验网址登陆测试'''
        title = '天翎体验环境'
        url = "http://dev01.teemlink.com:8080/obpm/"
        r = requests.get(url=url)
        code = r.status_code
        if(code!=200):
            function.send_mail(title)


    def test_message_website_login(self):
        '''短信平台网址登陆测试'''
        title = '天翎短信平台'
        url = "http://sms.teemlink.com/sms/"
        r = requests.get(url=url)
        code = r.status_code
        if(code!=200):
            function.send_mail(title)

    def test_forum_website_login(self):
        '''论坛网址登陆测试'''
        title = '天翎论坛'
        url = "http://www.teemlink.com/bbs/"
        r = requests.get(url=url)
        code = r.status_code
        if(code!=200):
            function.send_mail(title)



if __name__ == '__main__':
    unittest.main()