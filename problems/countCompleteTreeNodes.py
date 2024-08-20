# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node):
        num_of_nodes = 1

        if node.left:
            num_of_nodes += self.traverseTree(node.left)
        if node.right:
            num_of_nodes += self.traverseTree(node.right)
        
        return num_of_nodes


    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.traverseTree(root)