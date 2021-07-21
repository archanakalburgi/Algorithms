class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

'''read function'''
def read(head):
    temp = head
    while temp != None: 
        print(temp.val)
        temp = temp.next

# head = node1 = Node(11)
# node1.next = Node(22)
# node1.next.next = Node(33) 

# read(head)

'''read head outside function'''
# while head != None:
#     print(head.val)
#     head = head.next

# node1.next.next.next = Node(44)
# read(head)

'''read head outside function'''

# while head != None:
#     print(head.val)
#     head = head.next


def insert_at_start(head, newNode):
    newNode.next = head
    head = newNode
    return head 

def insertAtEnd_with_tail(tail, newNode): # with tail pointer
    tail.next = newNode
    tail = newNode
    return tail 

def insertAtEnd_without_tail(head, newNode):
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode 

def insert_after_value(head, val, newNode):
    temp = head
    while temp.val != val:
        temp = temp.next 
    temp2 = temp.next 
    temp.next = newNode
    newNode.next = temp2 

def delete_node(head, val):
    if head == None: # if head is null 
        return None 
    temp1 = head
    temp2 = head.next

    if head.val == val: # if only head had to be deleted 
        return head.next 

    while temp2 != None and temp2.val != val: # handles if val is not the linked list
        temp1 = temp1.next 
        temp2 = temp2.next

    if temp2:
        temp1.next = temp2.next
    return head 
    
    # if temp2.next != None: # if the given value is the last node in the linked list
    #     temp1.next = temp2.next  

def delete_with_dummy(head, val):
    dummy = Node('dummy')
    dummy.next = head
    temp1 = dummy
    temp2 = dummy.next

    while temp2 != None and temp2.val != val: 
        temp1 = temp1.next 
        temp2 = temp2.next
    
    if temp2:
        temp1.next = temp2.next
    
    return dummy.next


def length(head):
    temp = head 
    len = 0
    while temp.next != None:
        len += 1
        temp = temp.next 
    return len+1 # loop stops on the last node, so last node won't get counted, so return len+1

def length_recursive(head, len=0):
    temp = head
    if temp == None:
        return len

    return length_recursive(temp.next, len+1) 

head = None
head = insert_at_start(head, Node(10)) 
insertAtEnd_without_tail(head, Node(11))
insertAtEnd_without_tail(head, Node(100))
read(head)
head = delete_with_dummy(head, 102)
read(head) 
# read(head)
# head = insert_at_start(head, Node(20)) 
# head = insert_at_start(head, Node(30))
# head = insert_at_start(head, Node(40))

# '''inserting from the end with tail pointer'''

# tail = insertAtEnd_with_tail(tail, Node(0))
# tail = insertAtEnd_with_tail(tail, Node(-10))
# tail = insertAtEnd_with_tail(tail, Node(-20))
# tail = insertAtEnd_with_tail(tail, Node(-30))

# '''inserting from the end without tail pointer'''  

# insertAtEnd_without_tail(head, Node(100))
# insert_after_value(head, 20, Node(55)) 
# read(head)
# print("\n")
# delete_node(head, 55)
# read(head)

# print(length(head))
# print(length_recursive(head))


# print("tail:" )
# read(tail)