# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head.next and n==1:
            return None
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        if n==length:
            return head.next
        index=length-n
        count=0
        node1=head
        node2=head.next
        while count!=(index-1):
            count+=1
            node1=node1.next
            node2=node2.next
        if node2 and node2.next:
            node1.next=node2.next
        else:
            node1.next=None
        return head

        