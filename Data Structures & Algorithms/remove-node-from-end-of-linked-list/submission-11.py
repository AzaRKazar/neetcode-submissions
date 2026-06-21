# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        len=0
        curr=head 
        
        while curr!= None:
            len+=1
            curr=curr.next

        stop_pos=len-n
        curr=dummy
        for i in range(stop_pos):
            curr=curr.next

        curr.next=curr.next.next

        return dummy.next








