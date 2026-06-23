# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        curr2=slow.next
        slow.next=None
        curr1=head
        # reverse the second half
        prev=None
        curr=curr2
        while curr !=None:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        curr2=prev
        # alternating we have curr1 and curr2(reverse) merge them alternative
        firsthalf=curr1
        secondhalf=curr2
        while firsthalf!=None or secondhalf!=None:

            if firsthalf!=None:
                temp1=firsthalf.next
                firsthalf.next=secondhalf
                firsthalf=temp1
            if secondhalf!=None:
                temp2=secondhalf.next
                secondhalf.next=firsthalf
                secondhalf=temp2

     
        

