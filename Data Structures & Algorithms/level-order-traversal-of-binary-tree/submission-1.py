from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #BFS 
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue: 
            levelLen = len(queue)
            level = []
            for _ in range(levelLen):
                currNode = queue.popleft()
                level.append(currNode.val)
                if currNode.left: 
                    queue.append(currNode.left)
                if currNode.right: 
                    queue.append(currNode.right)
            res.append(level)
        return res
                


        