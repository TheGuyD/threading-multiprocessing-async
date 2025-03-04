import threading
from lxml import html
import requests
import time
import random

class YahooFinancePriceScheduler(threading.Thread):
    def __init__(self,input_queue,**kwargs):
        super().__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
        
    def run(self):
        while True:
            # this is a blocking operation
            val = self._input_queue.get()
            if val == 'DONE':
                break
            yahooFinanceWorkerworker = YahooFinanceWorker(val)
            price = yahooFinanceWorkerworker.get_price()
            print(price)

class YahooFinanceWorker:
    def __init__(self,symbol: str,**kwargs):
        super().__init__(**kwargs)
        self._symbol = symbol
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        BASE_URL = 'https://finance.yahoo.com/quote/'
        self._url = f'{BASE_URL}{self._symbol}/'
    
    def get_price(self):
        # time.sleep(30 * random.random())
        r = requests.get(self._url, headers=self._headers)
        print(self._url)
        if r.status_code != 200:
            print("Could not get the page")
            return 
        page_content = html.fromstring(r.text)
        price = float(page_content.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span')[0].text)
        return price
        