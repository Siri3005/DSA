# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        pre=head
        curr=head.next
        while curr!=None:
            if curr.val==val:
                pre.next=curr.next
                curr=curr.next
            else:
                pre=curr
                curr=curr.next
        return head
        