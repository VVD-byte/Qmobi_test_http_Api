import re
import requests
import json

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse


class HttpWorker(BaseHTTPRequestHandler):
    def set_response(self, code = 200):
        self.send_response(code)
        self.send_header('content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self.set_response()
        self.wfile.write(json.dumps(GetValue(self.path).resp_dat()).encode())


class GetValue:
    def __init__(self, url: str):
        self.value = 0
        self.url = url
        self.response = {
            'start_currency': '',
            'final_currency': '',
            'start_value': 0,
            'final_value': 0,
        }
        self.error_response = {
            'error_value': {'error': 'Exchange rate not found', },
            'error_url': {'error': 'incorrect data format: example - htttp://.../rub-usd?value=11', },
        }

    def get_dat(self):
        """Function return exchange rates"""
        r = requests.get(f'https://www.finanz.ru/valyuty{urlparse(self.url).path}').text
        if 'Валютный курс не найден' in r:
            return self.error_response['error_value']
        else:
            return re.findall(r'\d{1,4},\d{1,10}', r)[20].replace(',', '.')

    def resp_dat(self):
        """Function return data or error"""
        try:
            self.response['start_currency'] = urlparse(self.url).path.replace('/', '').split('-')[0]
            self.response['final_currency'] = urlparse(self.url).path.replace('/', '').split('-')[1]
        except:
            return self.error_response['error_value']
        curs = self.get_dat()
        if 'error' in curs:
            return self.error_response['error_value']
        try:
            self.response['start_value'] = re.findall(r'value=\d{0,100}[^&]{0,1}\d{0,3}', urlparse(self.url).query)[0].split('=')[1]
            self.response['final_value'] = round(float(self.response['start_value'])*float(curs), 4)
            return self.response
        except:
            return self.error_response['error_url']
