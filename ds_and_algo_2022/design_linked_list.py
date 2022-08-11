"""
LinkedList()
    get(index)
    addAtHead(val)
    addAtTail(val)
    addAtIndex(index, val)
    deleteAtINdex(index)
"""

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def get(self, index, head):
        idx = 0
        temp = head

        while idx < index:
            idx += 1
            temp = temp.next
        
        return temp

head = node1 = Node(21)
node2 = node1.next = Node(22)
node3 = node2.next = Node(23)
node4 = node3.next = Node(24)

linked_list = LinkedList()
result_node = linked_list.get(2, head) 

print(f"Node value : {result_node.val}") 
