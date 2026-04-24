# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = head
        size = 0 
        while curr: 
            size +=1
            curr = curr.next
        for i in range(0, size//2):
            res = res.next
        return res
            