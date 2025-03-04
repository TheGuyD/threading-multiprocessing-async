import time
import threading

# In this example we are creating threads to calculate the sum of squares and to sleep for a few seconds
# We are creating 5 threads to calculate the sum of squares and 5 threads to sleep for a few seconds
def calculate_sum_squares(numbers):
    sum_squares = 0
    for i in range(numbers):
        sum_squares += i ** 2
    
    print(f"Sum of squares: {sum_squares}")

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    
    current_threads = []
    for i in range(5):
        maximum_value = (i+1)*10000000
        
        #declare thread with a target and args
        t = threading.Thread(target=calculate_sum_squares, args=(maximum_value,))
        
        #initiate the thread
        t.start()
        
        #append the thread to the list of threads
        current_threads.append(t)
        
    for i in range(len(current_threads)):
        #wait for the thread to finish
        #block the caller until the thread is finished
        current_threads[i].join()

    print('calculating sum of squares took:', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    for seconds in range(1,6):
        #declare thread with a target and args
        t = threading.Thread(target=sleep_a_little, args=(seconds,))

        #initiate the thread
        t.start()
        
         #apend the thread to the list of threads
        current_threads.append(t)
    
    for i in range(len(current_threads)):
        #wait for the thread to finish
        #block the caller until the thread is finished
        current_threads[i].join()


    print('sleeping took:', round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()