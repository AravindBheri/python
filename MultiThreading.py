import threading
import time

def eat():
    time.sleep(3)
    print("Eating!!!!!!")
    
def drink():
    time.sleep(4)
    print("Drinking!!!")
    
def study():
    time.sleep(5)
    print("Studied!!!")
    
# eat()
# drink()
# study()

x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())