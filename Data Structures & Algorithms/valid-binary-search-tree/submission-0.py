# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidHelper(node, left, right):
            if not node: 
                return True
            if not (node.val < right and node.val > left): 
                return False
            left1 = isValidHelper(node.left, left, node.val)
            right1 = isValidHelper(node.right, node.val, right)
            return left1 and right1

        return isValidHelper(root, float("-inf"), float("inf"))
                



        

        