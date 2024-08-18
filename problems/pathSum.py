# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverseTree(self, node, path_sum, target):
        path_sum += node.val
        left = False
        right = False

        if node.left:
            left = self.traverseTree(node.left, path_sum, target)
        if node.right:
            right = self.traverseTree(node.right, path_sum, target)

        # Node is a leaf
        if not node.left and not node.right:
            if path_sum == target:
                return True
            else:
                return False

        return left or right


    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        result = self.traverseTree(root, 0, targetSum)
        return result