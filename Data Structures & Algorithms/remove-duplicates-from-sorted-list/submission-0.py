# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr:
            next = curr.next
            if curr.val in seen:
                prev.next = next
            else:
                seen.add(curr.val)
                prev = curr
            curr = next
        
        return dummy.next