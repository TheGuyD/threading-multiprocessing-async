import time

def calculate_sum_squares(numbers):
    sum_squares = 0
    for i in range(numbers):
        sum_squares += i ** 2
    
    print(f"Sum of squares: {sum_squares}")

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    calc_start_time = time.time()
    
    for i in range(5):
        calculate_sum_squares((i+1)*10000000)
    print('calculating sum of squares took:', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    for i in range(1,6):
        sleep_a_little(i)
    print('sleeping took:', round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()