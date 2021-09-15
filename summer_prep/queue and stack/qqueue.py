class Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity 
        self.front = 0
        self.end = 0
    
    def enqueue(self,val): 
        if self.end < self.capacity:
            self.items[self.end] = val
            self.end += 1
        else:
            raise(OverflowError)

    def dequeue(self):
        if self.front < self.end:
            self.items[self.front] = None
            self.front += 1
            # self.end -= 1
        else:
            raise(OverflowError)

    def get_front(self):
        return self.items[self.front-1]
        
    def get_end(self):
        print(self.end)
        return self.items[self.end-1] 

    def size(self):
        return len(self.items[self.front : self.end]) 

    # def is_empty(self):
    #     if self.items:
    #         return False
    #     return True 

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
# q.enqueue(60)
print(q.items)
print("front -> ", q.get_front())
print("end -> ", q.get_end())
print("length -> ", q.size())
print("\n")

q.dequeue()
print(q.items)
print("front -> ", q.get_front())
print("end -> ", q.get_end())
print("length -> ", q.size())