# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        # some sort of BFS with left true or not 

        if not root: 
            return []
        
        queue = deque([root])
        result = []
        left = True

        # while queue: 
        #     level_size = len(queue)
        #     level_queue = deque([queue.pop() for _ in range(level_size)])
        #     level = []
        #     for _ in range(level_size):
        #         if left:
        #             curr_node = level_queue.pop()
        #         else:
        #             curr_node = level_queue.popleft()
        #         level.append(curr_node.val)
        #         if curr_node.right:
        #             queue.append(curr_node.right)
        #         if curr_node.left:
        #             queue.appendleft(curr_node.left)

        #     result.append(level)
        #     left = not left
        # return result
        # left1 = true


        
        while queue: 
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                curr_node = queue.popleft()
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                        queue.append(curr_node.right)
            if not left: 
                level = reversed(level)
            result.append(level)
            left = not left
        return result

