# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        arr=[]
        temp=head
        while temp:
            arr.append(temp)
            temp=temp.next
        n=len(arr)
        i=0
        j=n-1
        while i<j:
            arr[i].next=arr[j]
            i+=1
            if i==j:
                break
            arr[j].next=arr[i]
            j-=1
        arr[i].next=None
