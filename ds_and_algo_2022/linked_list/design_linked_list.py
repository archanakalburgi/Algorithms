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

    def addAtHead(self, val, head):
        new_node = Node(val)
        new_node.next = head 
        head = new_node
        return head

    def addAtTail(self, val, head, tail=None):
        new_node = Node(val)
        if tail:
            tail.next = new_node
            tail = new_node
            return head
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
                if temp.next is None:
                    temp.next = new_node
                    temp = new_node
            return head

    def addAtIndex(self, index, val, head):
        new_node = Node(val)
        temp = head
        idx = 1
        while idx < index:
            print(temp.val)
            temp = temp.next
            idx+=1
        new_node.next = temp.next.next
        temp.next = new_node
        return temp


head = node1 = Node(21)
node2 = node1.next = Node(22)
node3 = node2.next = Node(23)
node4 = node3.next = Node(24)
node5 = node4.next = Node(25)

linked_list = LinkedList()

result_node = linked_list.get(2, head) 

# new_ll_insert_at_head = linked_list.addAtHead(10, head) 
# new_ll_insert_at_tail = linked_list.addAtTail(100, head, node4)
new_ll_insert_at_index = linked_list.addAtIndex(2, 88, head)

# print("\n")
# print(f"Node value : {result_node.val}") 
# print("\n")
# while new_ll_insert_at_head is not None:
#     print(f"{new_ll_insert_at_head.val}")
#     new_ll_insert_at_head = new_ll_insert_at_head.next

# while new_ll_insert_at_tail is not None:
#     print(f"{new_ll_insert_at_tail.val}")
#     new_ll_insert_at_tail = new_ll_insert_at_tail.next

while new_ll_insert_at_index is not None:
    print(f"{new_ll_insert_at_index.val}")
    new_ll_insert_at_index = new_ll_insert_at_index.next

