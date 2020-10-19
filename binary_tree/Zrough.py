'''
class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, data):
        self.items.insert(0, data)

    def addRear(self, data):
        self.items.append(data)

    def removeFront(self):
        if self.items: 
            self.items.pop()

    def removeRear(self):
        if self.items:
            self.items.pop(0)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def size(self):
        return len(self.items)  

    def peekFront(self):
        return self.items[-1]

    def peekRear(self):
        return self.item[0] 
'''

