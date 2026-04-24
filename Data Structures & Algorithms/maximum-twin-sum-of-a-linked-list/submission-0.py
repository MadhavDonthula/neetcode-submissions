# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        tail = head
        def getSize(theHead):
            size = 0
            while theHead: 
                theHead = theHead.next
                size +=1
            return size 
        iterate = getSize(tail) // 2
        for i in range(iterate):
            right, r = head, head
            stop_at = i 
            while stop_at > 0:
                r = r.next
                stop_at -= 1
            left = r 
            while r and r.next: 
                r = r.next
                right = right.next
            currSum = left.val + right.val 
            if currSum > max_sum: 
                max_sum = currSum
        return max_sum



