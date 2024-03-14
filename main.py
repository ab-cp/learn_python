import os, sys, time 
from datetime import datetime
from  multiprocessing import Process
import random
import inspect

SLEEP_TIME = 10

global running

def sub_process_1(count):
    this_function_name = inspect.currentframe().f_code.co_name
    running = True
    while running and count > 0:
        print("This is {} with id({}) from parent {}".format(this_function_name, os.getpid(), os.getppid()))
        time.sleep(SLEEP_TIME + random.randint(1,9) * 0.1)
        count = count - 1


def sub_process_2(count):
    this_function_name = inspect.currentframe().f_code.co_name
    running = True
    while running and count > 0:
        print("This is {} with id({}) from parent {}".format(this_function_name, os.getpid(), os.getppid()))
        time.sleep(SLEEP_TIME + random.randint(1,9) * 0.1)
        count = count - 1


def main():
    print("Hello World from main with id ({})".format(os.getpid()))
    print("Starting at {}".format(datetime.now()))
    sbp = []
    p = Process(target=sub_process_1, args=(10,))
    p.start()

    sbp.append(p)
    p = Process(target=sub_process_2, args=(20,))
    p.start()

    sbp.append(p)
    running = True
    while running:
        ch = input("Press a key")
        running = False
    print("Key pressed")
    time.sleep(SLEEP_TIME + random.randint(1,9) * 0.1)        
    for p in sbp:
        p.join()
    print("Exiting at {}".format(datetime.now()))       
    sys.exit()



if __name__ == "__main__":
    print("This is main function")
    main()