import requests
import random
import base64
import string
from urllib.parse import quote
from lxml import etree
def fofascan(cookie,query):
    while 1:
        query = query.replace(',',"&&")[:-2]
        url = 'https://fofa.so'
        strs=string.ascii_lowercase
        domainlist=[]
        dc=''
        for _ in range(random.randint(1,2)):
            dc+=random.choice(strs)
        query+="{}".format(dc) #添加字符绕过限制
        for page in range(1,6):
            yufa=base64.b64encode(query.encode()).decode()
            q=quote(query)
            UserAgent = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50","Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0","Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"]
            header = {
                    "User-Agent": random.choice(UserAgent),
                    "Cookie":"_fofapro_ars_session={};referer_url={};search_history={}".format(cookie,quote(url),quote(query)),
                    "Referer":"{}".format(quote(url))
                    }
            url = 'https://fofa.so/result?page={}&qbase64={}&q={}&full=true'.format(page,quote(yufa),q)
            html = requests.get(url=url,headers=header).text
            selector = etree.HTML(html)
            domain = selector.xpath('//*[@id="ajax_content"]/div/div[1]/div[1]/a/text()')
            domain = [value.strip('\n').strip(' ') for value in domain if len(value.strip('\n').strip(' ')) != 0]
            for i in domain:domainlist.append(i)
        if domainlist==[]:continue
        else:
            return domainlist
