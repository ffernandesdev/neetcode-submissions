# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_nodes = set()

        curr = headA
        while curr:
            a_nodes.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in a_nodes:
                return curr
            curr = curr.next
        
        return None