from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
    
def main():
    
    print(cpu_count())
    
    a = Process(target=counter, args=(2500000000,))
    a.start()
    
    b = Process(target=counter, args=(25000000000,))
    b.start()
    
    c = Process(target=counter, args=(25000000000,))
    c.start()
    
    d = Process(target=counter, args=(25000000000,))
    d.start()
    
    
    print("FINISHED IN ", time.perf_counter(), "SECONDS")
    
if __name__ == "__main__":
    main()