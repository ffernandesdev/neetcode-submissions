"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dps(root):
            if not root:
                return

            for node in root.children:
                dps(node)

            res.append(root.val)
                
        dps(root)
        return res