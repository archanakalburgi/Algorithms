def insert(head, val, ListNode):
    temp = head
    while temp.val != val:
        temp = temp.next
    temp2 = temp.next
    temp.next = ListNode
    ListNode.next = temp2 