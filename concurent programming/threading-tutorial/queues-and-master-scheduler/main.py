import time
from multiprocessing import Queue
from Workers.WikiWorker import WikiWorker
from Workers.YahooFinanceWorker import YahooFinancePriceScheduler

############################################## threading with queues and master scheduler ##############################################
# *queues* are used to pass data between threadsin addition to that they are thread-safe
# *master scheduler* is a thread that will manage the other threads
# *producer-concumer* pattern is used to pass data between threads, the producer will put data into the queue and the concumer will get the data from the queue
# *concumer* is the YahooFinancePriceScheduler 
# *producer* is the WikiWorker
def main():
    symbol_queue = Queue()
    scraper_start_time = time.time()
    wikiWorker = WikiWorker()
    
    yahoo_finance_price_scheduler_threads = []
    
    num_yahoo_finance_price_workers = 4

    for worker in range(num_yahoo_finance_price_workers):
        # yahooFinancePriceScheduler is the concumer, it will get the data from the queue independently of the other threads
        yahooFinancePriceScheduler=YahooFinancePriceScheduler(input_queue=symbol_queue)
        
        # in case we have multiple threads (workers) we need to keep track of them
        yahoo_finance_price_scheduler_threads.append(yahooFinancePriceScheduler)
        
    # WikiWorker is the producer
    for symbol in wikiWorker.get_sp_500_companies():
        # putting symbols into the queue    
        symbol_queue.put(symbol)
    
    
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')
    
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()
    
    print('Extracting time took:', round(time.time() - scraper_start_time, 1))

if __name__ == '__main__':
    main()