# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #only need the heads of each list at the start
        # the heap only holds k items at one time
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))
        dummy = ListNode(0)
        tail = dummy 
        while minHeap:
            value, index, currNode = heapq.heappop(minHeap)
            tail.next = currNode
            tail = tail.next
            if currNode.next:
                heapq.heappush(minHeap, (currNode.next.val, index, currNode.next))
        return dummy.next



        