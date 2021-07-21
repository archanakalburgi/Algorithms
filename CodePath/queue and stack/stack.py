class Stack:
    def __init__(self, capacity) -> None:
        self.items = [None] * capacity 
        self.top = -1
        self.capacity = capacity 

    def add(self, val):
        self.top += 1
        # print(self.top)
        if self.top < self.capacity:
            self.items[self.top] = val
        else:
            raise(OverflowError) 

    def delete(self):
        if self.top > 0:
            self.items[self.top] = None
            self.top -= 1 
            # print(self.top)
        else:
            print("Stack is empty")

    def peek(self):
        # print(self.items[self.top])
        return self.items[self.top]

    def size(self):
        return len(self.items[0:self.top+1])  

    # def isEmpty(self):
    #     return len(self.items) == 0

s = Stack(5)
# s.add(10)
# s.add(20)
# s.add(30) 
# s.add(40)
# s.add(50)
# print("last element -> ", s.peek())
print(s.items)
print("size -> ",s.size())
print("\n")
s.delete()
print("last element -> ",s.peek())
print(s.items)
print("size -> ",s.size())