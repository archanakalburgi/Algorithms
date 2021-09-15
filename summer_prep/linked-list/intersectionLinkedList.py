class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def intersectionUsingSet(head1, head2):
    temp1,temp2 = head1,head2
    node_set = set()
    while temp1 != None:
        node_set.add(temp1) # adding nodes instead of val
        temp1 = temp1.next
    # print(node_set)

    while temp2 != None:
        if temp2 in node_set: # checking for temp2 in node_set and not temp2.val
            return temp2 
        temp2 = temp2.next
    return None

def intersectionWithoutDS(head1, head2): # O(m+n) 
    def length(head, len=0):
        temp = head
        if temp == None:
            return len
        return length(temp.next, len+1) 

    temp1 = head1
    temp2 = head2

    length_LL1 = length(temp1)
    length_LL2 = length(temp2)
    # print(length_LL1, length_LL2)

    diff = abs(length_LL1-length_LL2)

    if length_LL1 < length_LL2:
        for i in range(diff):
            temp2 = temp2.next 

    if length_LL1 > length_LL2:
        for i in range(diff):
            temp1 = temp1.next 

    # print(temp1.val, temp2.val)

    while temp1 != None and temp2 != None:
        # if temp1.val == temp2.val: # gives same value, instead check the entire node 
        if temp1 == temp2:
            return temp2 
        temp1 = temp1.next
        temp2 = temp2.next 

    return None 


head1 = node1 = Node(10)
node2 = node1.next = Node(20)
# node3 = node2.next = Node(30)

head2 = nodeA = Node(100)
nodeB = nodeA.next = Node(200)
nodeC = nodeB.next = Node(300)

node2.next = nodeC.next = nodeY = Node(50) 
nodeZ = nodeY.next = Node(60) 

# print(intersectionUsingSet(head1, head2)) 
print(intersectionWithoutDS(head1, head2).val) 