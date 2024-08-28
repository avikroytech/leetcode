# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, node):
        l_child = node.left
        r_child = node.right

        node.left = r_child
        node.right = l_child

        if node.left:
            self.invertTree(node.left)
        if node.right:
            self.invertTree(node.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        self.invertTree(root)

        return root