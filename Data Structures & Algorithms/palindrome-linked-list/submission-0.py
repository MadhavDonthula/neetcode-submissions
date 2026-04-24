# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        check1 = head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        slow = prev
        while check1 and slow: 
            if check1.val != slow.val: 
                return False
            check1 = check1.next
            slow = slow.next
        return True
        


             
