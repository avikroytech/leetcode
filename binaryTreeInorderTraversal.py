# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeTraversal(self, node):
        nodes = [node.val]

        if node.left:
            result = self.treeTraversal(node.left)
            nodes = result + nodes
        if node.right:
            result = self.treeTraversal(node.right)
            nodes += result
        
        return nodes


    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return root
        elif not root.left and not root.right:
            return [root.val]
        
        nodes = [root.val]

        if root.left:
            result = self.treeTraversal(root.left)
            nodes = result + nodes
        if root.right:
            result = self.treeTraversal(root.right)
            nodes += result
        
        return nodes