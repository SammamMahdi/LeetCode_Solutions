# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        i, j = 0, len(lst)-1
        while j>i:
            if lst[j] !=lst[i]:
                return False
            j-=1
            i+=1
        return True
        