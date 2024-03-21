# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        curr = head
        newHead = None
        while curr:
            newHead = curr
            curr = curr.next
            newHead.next = dummy
            dummy = newHead
        return newHead 
            
            
        