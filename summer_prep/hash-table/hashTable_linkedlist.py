class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class HashTable:
    def __init__(self) -> None:
        self.array = [None] * 26 

    def hashFunction(self, key):
        key = key.lower()
        return ord(key) % 97 

    def get(self, key): # get a certain value from the hashtable 
        index = self.hashFunction(key)
        if self.array[index] == None: # if key is not present in the array 
            raise KeyError("Key Not Found") 
        return self.array[index]

    def put(self, key, value) -> int:
        index = self.hashFunction(key)

        if self.array[index] == None:
            self.array[index] = ListNode(value)
        
        else:
            head = self.get(key)  
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = ListNode(value)

    def remove(self, key):
        index = self.hashFunction(key)
        self.array[index] = None

ht = HashTable()
ht.put('A',10) 
ht.put('a', 20)
ht.put('a', 30)
ht.put('B',20)
ht.put('c',30) 
ht.put('z', 90)


def read(head):
    temp = head
    while temp != None: 
        print(temp.val)
        temp = temp.next

for item in ht.array:
    print("-----")
    if item == None:
        print("None")
    read(item)

# print(ht.array)
