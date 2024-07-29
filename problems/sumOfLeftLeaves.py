# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeTraversal(self, node, nodeType):
        left = []

        if node.left:
            result = self.treeTraversal(node.left, 'left')
            left += result
        if node.right:
            result = self.treeTraversal(node.right, 'right')
            left += result
        
        if nodeType == 'left' and not node.left and not node.right:
            left.append(node.val)
        
        return left


    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left = []

        if root.left:
            result = self.treeTraversal(root.left, 'left')
            left += result
        if root.right:
            result = self.treeTraversal(root.right, 'right')
            left += result

        if root.left == None and root.right == None:
            return 0
        
        return sum(left)
