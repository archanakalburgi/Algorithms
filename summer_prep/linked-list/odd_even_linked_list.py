# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        i = j = 1
        nodelist = []
        temp1 = temp2 = head

        while temp1 != None:
            if i%2 != 0:
                nodelist.append(temp1.val)
            temp1 = temp1.next
            i+=1
        
        while temp2 != None:
            if j%2 == 0:
                nodelist.append(temp2.val)
            temp2 = temp2.next
            j+=1
        
        dummy = ListNode("dummy")
        prev = dummy
        for k in range(len(nodelist)):
            temp = ListNode(nodelist[k])
            prev.next = temp 
            prev = temp 
        return dummy.next 

head = node1 = ListNode(10)
node2 = node1.next = ListNode(20)   
node3 = node2.next = ListNode(30)
node4 = node3.next = ListNode(40)

s = Solution()
newhead = s.oddEvenList(head) 

while newhead != None: 
    print(newhead.val)
    newhead = newhead.next
