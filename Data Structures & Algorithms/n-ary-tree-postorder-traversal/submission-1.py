"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []

        while stack:
            node = stack.pop()

            if not node:
                continue
            
            for child in node.children:
                stack.append(child)

            res.append(node.val)
        
        l, r = 0, len(res) - 1

        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r  -= 1

        return res