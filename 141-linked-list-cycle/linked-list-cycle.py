# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        res=set()
        while head:
            if head in res:
                return True
            else:
                res.add(head)
            head=head.next
        return False