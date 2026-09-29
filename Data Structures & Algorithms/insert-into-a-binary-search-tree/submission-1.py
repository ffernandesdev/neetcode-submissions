# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        parent = None

        while curr:
            parent = curr
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left

        # tree is empty
        if not parent:
            return TreeNode(val)
        elif val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        
        return root