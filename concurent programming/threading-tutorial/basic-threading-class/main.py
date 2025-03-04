from workers.SquaredSumWorkers import SquaredSumWorkers
from workers.SleepyWorkers import SleepyWorkers
import time

# threading with classes 
def main():
    calc_start_time = time.time()
    current_workers = []
    for i in range(5):
        maximum_value = (i+1)*10000000
        squaredSumWorker = SquaredSumWorkers(numbers=maximum_value)
        current_workers.append(squaredSumWorker)
        
    for i in range(len(current_workers)):
        current_workers[i].join()
    
    print('calculating sum of squares took:', round(time.time() - calc_start_time, 1))
    
    sleep_start_time = time.time()
    
    for seconds in range(1, 6):
        sleepyWorker = SleepyWorkers(seconds=seconds)
        current_workers.append(sleepyWorker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
    
    print('sleeping took:', round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()