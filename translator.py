import http.client
import hashlib
import json
import urllib
import random

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'
httpClient = None
sub_url = '/api/trans/vip/translate'

class Translator():

    def _do_request(self, myurl):
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')

        http_client.request('GET', myurl)
        # response是HTTPResponse对象
        response = http_client.getresponse()
        json_response = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(json_response)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst



    def translate(self, content, from_lang, to_lang):
        q = content
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = sub_url + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(
            salt) + '&sign=' + sign
        return self._do_request(myurl)




