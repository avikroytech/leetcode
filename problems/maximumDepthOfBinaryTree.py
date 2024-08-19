# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, node, depth):
        depth += 1

        if not node.left and not node.right:
            return depth
        else:
            leftDepth = depth
            rightDepth = depth

            if node.left:
                leftDepth = self.traverseTree(node.left, depth)
            if node.right:
                rightDepth = self.traverseTree(node.right, depth)

            if leftDepth > rightDepth:
                return leftDepth
            else:
                return rightDepth

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.traverseTree(root, 0)