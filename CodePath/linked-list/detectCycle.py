class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detectCycle(head):
    if head == None or head.next == None:
        return False 

    slow = head
    fast = head.next 

    while fast != None and fast.next != None:
        if fast.next == slow: #or slow == fast, if we do slow==fast, pointer hs to mode to the net node which will take some extra time, so we do fast.next == slow
            return True
        
        slow = slow.next
        fast = fast.next.next 

    return False

head = node1 = Node(10)
node2 = node1.next = Node(20)
node3 = node2.next = Node(30)
node4 = node3.next = Node(40)
node4.next = node2 

print(detectCycle(head))