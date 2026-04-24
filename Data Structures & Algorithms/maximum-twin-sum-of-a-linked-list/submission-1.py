# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0 
        slow, fast = head, head
        start = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        slow = prev
        while slow: 
            currSum = start.val + slow.val
            if currSum > max_sum: 
                max_sum = currSum
            start = start.next
            slow = slow.next
        return max_sum



