# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else:
                    break
        dummyList=ListNode(0)
        curr=dummyList
        for num in arr:
            curr.next=ListNode(num)
            curr=curr.next
        return dummyList.next

        