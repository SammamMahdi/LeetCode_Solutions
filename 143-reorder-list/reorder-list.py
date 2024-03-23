# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i, j = 0, len(nodes) - 1
        new_order = []
        while i < j:
            new_order.append(nodes[i])
            new_order.append(nodes[j])
            i += 1
            j -= 1
        if i == j:
            new_order.append(nodes[i])
        for i in range(len(new_order) - 1):
            new_order[i].next = new_order[i + 1]
        new_order[-1].next = None
             
            

            
        

            
        