''' designing a hash table with keys of type character and values of type integer 
example 
{A:1,
B:2,
C:3,
D:4}'''

class HashTable:
    def __init__(self): # none
        self.array = [None] * 26 # size = 26 (because only 26 alphabets)

    def hashFunction(self, key):
        key = key.lower()
        return ord(key) % 97 

    def get(self, key): # get a certain value from the hashtable 
        index = self.hashFunction(key)
        if self.array[index] == None: # if key is not present in the array 
            raise KeyError("Key Not Found") 
        return self.array[index] 
    
    def put(self, key, value):
        index = self.hashFunction(key) 
        if self.array[index] == None: # places value only if there is place 
            self.array[index] = value 
        else:  # if slot is filled 
            
            while self.array[index] != None: # goes to next empty slot 
                index = (index+1) % 26 # if key = z (last slot), indexing should start from 0 to check for empty slots
            self.array[index] = value
            '''problem :  put('z', 90), put('z', 200), 200 is array[4]
            get(z) rises problem because array['z'] = array[26] = 90, but we want 200
            solution : chaining'''

    def remove(self, key):
        index = self.hashFunction(key)
        self.array[index] = None

ht = HashTable()
# print(ht.array)
ht.put('A',10) 
ht.put('B',20)
ht.put('c',30) 
ht.put('z', 90)
print(ht.array)
ht.put('A',100) 
ht.put('z', 200)
print(ht.array)
# # print(ht.get("B"))
# print(ht.array)

# ht.remove("B")
# print(ht.array)  

# print(ht.get("B")) 