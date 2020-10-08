# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2018/3/25
# @Author  : h4rdy <with.h4rdy@gmail.com>
# @File    : api.py

import base64
import requests


class FofaAPI(object):

    def __init__(self, email, key):
        self.email = email
        self.key = key
        self.base_url = 'https://fofa.so'
        self.search_api_url = '/api/v1/search/all'
        self.login_api_url = '/api/v1/info/my'
        self.get_userinfo()

    def get_userinfo(self):
        try:
            url = '{url}{api}'.format(url=self.base_url, api=self.login_api_url)
            data = {"email": self.email, 'key': self.key}
            req = requests.get(url, params=data)
            return req.json()
        except requests.exceptions.ConnectionError:
            error_msg = {"error": True, "errmsg": "Connect error"}
            return error_msg

    def get_data(self, query_str='', page=1, fields='host,ip,port'):
        try:
            url = '{url}{api}'.format(url=self.base_url, api=self.search_api_url)
            query_str = bytes(query_str, 'utf-8')
            data = {'qbase64': base64.b64encode(query_str), 'email': self.email, 'key': self.key, 'page': page,
                    'fields': fields}
            req = requests.get(url, params=data, timeout=10)
            return req.json()
        except requests.exceptions.ConnectionError:
            error_msg = {"error": True, "errmsg": "Connect error"}
            return error_msg