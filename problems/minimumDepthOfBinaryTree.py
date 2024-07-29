# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverseTree(self, node):
        if not node:
            return 0
        
        depth = 1

        if not node.left and not node.right:
            return depth

        leftDepth = self.traverseTree(node.left)
        rightDepth = self.traverseTree(node.right)

        condition = leftDepth + depth < rightDepth + depth

        if leftDepth > 0 and rightDepth > 0:
            return leftDepth + depth if condition else rightDepth + depth
        else:
            return leftDepth + depth if rightDepth == 0 else rightDepth + depth
        

    def minDepth(self, root: TreeNode) -> int:
        depth = self.traverseTree(root)

        return depth