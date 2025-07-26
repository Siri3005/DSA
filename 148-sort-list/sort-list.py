# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        dummyNode=ListNode(0)
        curr=dummyNode
        for num in arr:
            curr.next=ListNode(num)
            curr=curr.next
        return dummyNode.next