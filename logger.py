import heapq

class Logger:
    def __init__(self): 
        self.store = {}
        self.heap = []
        
    def start(self, pid, ts):   #O(1)
        if pid not in self.store:
            self.store[pid] = ts
        
    def end(self, pid, ts):    #O(logn)
        if pid in self.store:
            heapq.heappush(self.heap, (self.store[pid], ts, pid))
            del self.store[pid]
    
    def print(self):     #O(n)
        tmp = self.heap[:]
        
        while len(tmp) > 0:
            start, end, pid = heapq.heappop(tmp)
            
            print('{} started at {} and ended at {}'.format(pid, start, end))
