# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        def getSize(node):
            siz = 0 
            while node: 
                siz +=1
                node = node.next
            return siz
        
        size = getSize(head)
        iterate = size - n
        
        for i in range(iterate):
            tail = tail.next
        if tail.next:
            tail.next = tail.next.next
        return dummy.next

        