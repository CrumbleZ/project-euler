
# ===== IMPORTS =============
import time

class pe_timer:
    _timer = 0

    @staticmethod
    def start():
        print("Answer : ", end="")
        pe_timer._timer = time.perf_counter()

    @staticmethod
    def stop():
        print("Execution time : {0:f}".format(round(time.perf_counter() - pe_timer._timer, 5)))

def xor_swap(a, b):
    a = a ^ b
    b = b ^ a
    a = a ^ b
