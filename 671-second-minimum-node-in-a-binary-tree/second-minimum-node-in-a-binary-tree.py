# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        self.res=[]
        def helper(root):
            if not root:
                return
            self.res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        sorted_vals=sorted(list((set(self.res))))
        return sorted_vals[1] if len(sorted_vals)>1 else -1