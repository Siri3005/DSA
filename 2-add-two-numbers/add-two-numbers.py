# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1=''
        str2=''
        while l1:
            str1=str(l1.val)+str1
            l1=l1.next
        while l2:
            str2=str(l2.val)+str2
            l2=l2.next
        res=int(str1)+int(str2)
        res_str=str(res)[::-1]
        dummy=ListNode(0)
        tail=dummy
        for i in range(len(res_str)):
            tail.next=ListNode(int(res_str[i]))
            tail=tail.next
        return dummy.next
        
        