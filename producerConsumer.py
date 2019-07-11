from threading import Condition, Thread, Lock
import time
import random

queue = []
qt = 0
lock = Lock()
condition = Condition()
nums = list(range(10))

class Consumer(Thread):
    def run(self):
        global queue
        global nums
        while True:
            condition.acquire()
            global qt
            qt = int(random.random()*5)
            if len(queue)<qt:
                print("not enough prods to consume")
                condition.wait()
                print("producer notified")
            for i in range(qt):
                num = queue.pop(0)
                nums.append(num)
                print("consumed", num)
            condition.release()
            qt = 0
            time.sleep(random.random())

class Producer(Thread):
    def run(self):
        global nums
        global queue
        while True:
            condition.acquire()
            if qt:
                for i in range(qt-len(queue)):
                    num = random.choice(nums)
                    queue.append(num)
                    nums.remove(num)
                    print("produced",num)
                condition.notify()
            num = random.choice(nums)
            queue.append(num)
            nums.remove(num)
            print("produced",num)
            condition.release()
            time.sleep(random.random())
Producer().start()
Consumer().start()

            
