import time

from Workers.WikiWorker import WikiWorker
from Workers.YahooFinanceWorker import YahooFinanceWorker

# threading with classes 
def main():
    scraper_start_time = time.time()
    current_workers = []
    wikiWorker = WikiWorker()
    for symbol in wikiWorker.get_sp_500_companies():    
        yahooFinanceWorker = YahooFinanceWorker(symbol = symbol)
        current_workers.append(yahooFinanceWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
    
    print('Extracting time took:', round(time.time() - scraper_start_time, 1))

if __name__ == '__main__':
    main()