# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        tail = head 
        while tail and tail.next: 
            if tail.next.val == val:
                tail.next = tail.next.next
            else: 
                tail = tail.next

        return head 