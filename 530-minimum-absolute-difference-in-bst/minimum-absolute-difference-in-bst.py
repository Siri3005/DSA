# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        self.minim=float('inf')
        self.prev=None
        def helper(root):
            if not root:
                return 
            helper(root.left)
            if self.prev is not None:
                self.minim=min(self.minim,abs(root.val-self.prev))
            self.prev=root.val
            helper(root.right)
        helper(root)
        return self.minim

        