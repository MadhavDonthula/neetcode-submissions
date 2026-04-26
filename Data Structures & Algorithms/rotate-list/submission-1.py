# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #rotate by k righ means finding new tail" 
        #new head = n-k from the start 0 indexed 
        #new tail = n-k-1
        #make a circle and cut 

        if not head or not head.next or k == 0: 
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0: 
            return head
        tail.next = head #connect old tail to old head. 
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
        