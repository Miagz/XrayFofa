import requests
import base64
class FofaAPI(object):
    def __init__(self,email,key):
        self.email = email
        self.key = key
    def get_user_is_vip(self):
        get_user_info = 'https://fofa.so/api/v1/info/my'
        data={'email':self.email,'key':self.key}
        info = requests.get(get_user_info,params=data)
        if 'errmsg' in info.json():return info.json()['errmsg']
        
    def get_data(self,query,page=1,fields='host'):
        get_data_info='https://fofa.so/api/v1/search/all'
        if self.get_user_is_vip():
            return self.get_user_is_vip()
        query=query.replace(",","&&")[:-2]
        qbase64 = base64.b64encode(query.encode()).decode()
        data = {'qbase64':qbase64,'email':self.email,'key':self.key,'page':page,'fields':fields}
        info = requests.get(get_data_info,params=data,timeout=5)
        return info.json()
