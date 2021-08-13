class Solution:
    def swapPairs(self, head):
            
        if not head or not head.next:
            return head
        
        prev = None
        newHead = None
        temp1 = head

        while temp1 and temp1.next:
            temp2 = temp1.next
            temp1.next = temp2.next
            temp2.next = temp1
            if not newHead:
                newHead = temp2
            else :
                prev.next = temp2

            prev = temp1
            temp1 = temp1.next
        
        return newHead 

    def subarray(self, array, start, end, sub):
        if end == len(array):
            return sub
        if array:
            if start > end:
                return self.subarray(array,0,end+1,sub)
            else:
                sub.append(array[start:end+1])
                return self.subarray(array,start+1,end,sub)
        return sub
