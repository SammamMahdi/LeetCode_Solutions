# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1 = list1
        i = 1
        while i <= b:
            if i == a:
                before_a = temp1
            if i == b:
                after_b = temp1.next
            temp1 = temp1.next
            i += 1
        temp2 = list2
        while temp2.next:
            temp2 = temp2.next
        before_a.next = list2
        temp2.next = after_b.next
        return list1
        