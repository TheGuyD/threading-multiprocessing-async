import threading
import time


class SleepyWorkers(threading.Thread):
    # **kwargs is a dictionary that will receive any additional arguments
    def __init__(self, seconds, **kwargs):
        self._seconds = seconds
        super().__init__(**kwargs)
        self.start()

    def _sleep_a_little(self):
        time.sleep(self._seconds)

    def run(self):
        self._sleep_a_little()
