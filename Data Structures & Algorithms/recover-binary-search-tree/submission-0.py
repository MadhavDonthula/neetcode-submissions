# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None

        def inOrder(node):
            if not node: 
                return 
            
            inOrder(node.left)

            curr_node = node.val
            if self.prev and curr_node < self.prev.val:
                if self.first is None: 
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node
            self.prev = node
            inOrder(node.right)
        
        inOrder(root)

        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        if self.first and self.last is None:
            self.first.val, self.middle.val = self.middle.val, self.first.val
