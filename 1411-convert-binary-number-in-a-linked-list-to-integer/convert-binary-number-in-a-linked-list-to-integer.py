# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        arr=[]
        while head:
            arr.append(str(head.val))
            head=head.next
        string=''.join(arr)
        return int(string,2)