import queue
# class for creating a binary tree node
class BinTreeNode :
    def __init__(self, data):
        self.heap = []
        self.data = data
        self.left = None
        self.right = None

def parent(i):
    return (i-1)//2

def left_child(i):
    return i*2 + 1 

def right_child(i):
    return i*2 + 2

def has_parent(i):
    return parent(i) >= 0

def has_left_child(i):
    return left_child < len(heap)

def has_right_child(i):
    return right_child(i) < len(heap) 
    
    # pre order traversal
    ''' in this traversal, we visit the node first and then traverse left and the right subtrees in order
    reprat the same till we hit a null child link  '''
def preorderTrav(subtree):
    if subtree id not None :
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
    ''' if subtree is not null:
            the node is first visited
            then the two nodes are visited
            
        if subtree is null :
            it means the BT is empty 
            or we are trying to follow a non existent link for one or both of the children'''

def inorderTrav(subtree):
    if subtree id not None :
        preorderTrav(subtree.left)
        print(subtree.data)
        preorderTrav(subtree.right)

def postorderTrav(subtree):
    if subtree id not None :
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
        print(subtree.data)

def breadthFirstTrav(bintree):
        # create a queue and add the root node 
    Queue q
    q.enqueue (bintree)
    while not q.is_empty():
        # remove next node from the queue and vist it
        node = q.dequque()
        print(node.data)
        # add two childer to the queue 
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right) 

#  array implementation of max heap 
class MaxHeap():
    # Create a max-heap with maximum capacity of maxSize.
    def __init__( self, maxSize ):
        self.count = 0 # keeps track of how many element sis added to the heap/array
        self.elements = []  # pg 396 line 5 


    def __len__(self):
        return self.count 

    def capacity(self):
        return self.len(self.elements) 

    def add(self, value):
        assert self.count < self.capacity(), "Cannot add to a full heap."
        self.elements[self.count] = value
        self.count += 1 
        self.siftUp( self.count - 1 ) # move the value up the tree 

    def extract(self):
        assert self.count > 0, "Cannot extract from an empty heap."
        value = self.elements[0] # copying the first element 
        slef.count -= 1
        self.elements[0] = self.elements[self._count]
        self._siftDown(0) 

    def siftUp(self, index):
        if index > 0:
            parent = index // 2 
            if self.elements[index] > self.elements[parent]: # if true the we swap the elements 
                temp = self.elements[index] 
                self.elements[index] = self.elements[parent]
                self.elements[parent] = temp 
                self.siftUp(parent)

    def siftDown(self, index):
        left = 2*index + 1
        right = 2*index + 2 
        # we need to check for the largest value 
        largest = index 
        if left < count and self.elements[left] >= self.elements[largest]: 
            largest = left
        if right < count and self.elements[right] >= self.elements[largest]: 
            largest = right 
        if largest != index:
            temp = self.elements[index] 
            self.elements[index] = self.elements[largest]
            self.elements[largest] = temp 
            self.siftDown(largest)

# heapsort implementation 
def heapsort(sequence):
    n = len(sequence)
    # building maxheap
    for i in range(n):
        siftUp(sequence,i)
    
    # extracting from the heap to get sorted array
    for j in range(n-1, 0, -1):
        temp = sequence[j]
        sequence[j] = sequence[0]
        sequence[0] = temp 
        siftDown(sequence, j-1, 0) 
