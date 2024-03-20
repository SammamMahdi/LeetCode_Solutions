# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        while l1 or l2:
            if l1:
                n1 += str(l1.val)
                l1 = l1.next
            if l2:
                n2 += str(l2.val)
                l2 = l2.next
        n1 = int(n1[::-1])
        n2 = int(n2[::-1])
        n3 = n1 + n2
        n3 = str(n3)[::-1]
        head = ListNode(int(n3[0]))
        current = head
        for i in range(1, len(n3)):
            current.next = ListNode(int(n3[i]))
            current = current.next
        return head