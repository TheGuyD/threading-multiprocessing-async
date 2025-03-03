import threading

class SquaredSumWorkers(threading.Thread):
    # **kwargs is a dictionary that will receive any additional arguments
    def __init__(self,numbers,**kwargs):
        self._numbers = numbers
        super().__init__(**kwargs)
        self.start()

    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._numbers):
            sum_squares += i ** 2
        
        print(f"Sum of squares: {sum_squares}")
        
    def run(self):
        self._calculate_sum_squares()
        