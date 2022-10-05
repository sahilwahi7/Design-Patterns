from concurrent import futures
from pickle import TRUE
import queue
import threading
import datetime
import time

NUM_THREADS=10
q=queue.Queue()
class rateLimiter:

    def grantAccess():
        pass

class LeakyBucket(rateLimiter):
    bucket_s=[]
    def __init__(self,capacity):
        self.capacity=capacity

    def grantAccess(self):
        if len(self.bucket_s)<self.capacity:
            self.bucket_s.append(1)
            return True
        return False


class BucketCreater:
    _bucket={}
    def __init__(self,id):
        self.id=id
        self._bucket[self.id]=LeakyBucket(10)
    
    def accessApplication(self):
        if self._bucket[self.id].grantAccess():
            print("Request passess")

        else:
            print("Rate limited")

    def emptyApplication(self):
        self._bucket[self.id].bucket_s =[]
        
        
t1=time.time()
userBucket=BucketCreater(1)
with futures.ThreadPoolExecutor(max_workers=10) as exe:
    for i in range(12):
         exe.submit(userBucket.accessApplication())
t2=time.time()
print(t2-t1)
userBucket.emptyApplication()
