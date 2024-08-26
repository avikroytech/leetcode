# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node):
        nodes = [node]
        if not node.left and not node.right:
            return nodes

        if node.left:
            nodes += self.traverseTree(node.left)
        if node.right:
            nodes += self.traverseTree(node.right)

        return nodes

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return root
        
        nodes = self.traverseTree(root)
        
        for i in range(len(nodes)-1):
            node = nodes[i]
            node.left = None
            node.right = nodes[i+1]

        nodes[-1].left = nodes[-1].right = None

        return nodes[0]