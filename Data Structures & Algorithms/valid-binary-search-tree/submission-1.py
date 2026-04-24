# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        res = []
        stack = []
        curr = root

        while stack or curr: 
            while curr: 
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if res: 
                last_elem = res[-1]
                if curr.val > last_elem: 
                    res.append(curr.val)
                else: 
                    return False
            if not res:
                res.append(curr.val)
            curr = curr.right
        return True
        

     


        

        