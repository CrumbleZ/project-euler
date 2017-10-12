import time

class timer:
    _time = 0

    @staticmethod
    def start():
        print("Answer : ", end="")
        timer._time = time.perf_counter()

    @staticmethod
    def stop():
        print("Execution time : {0:5f}".format(round(time.perf_counter() - timer._time, 5)))
