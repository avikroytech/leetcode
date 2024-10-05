# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node):
        nodes = []

        if node:
            nodes = self.traverseTree(node.left)
            nodes.append(node.val)
            nodes += self.traverseTree(node.right)

        return nodes

    def getMinimumDifference(self, root: TreeNode) -> int:
        nodes = self.traverseTree(root)

        difference = 10**5

        for i in range(len(nodes)-1):
            node_diff = abs(nodes[i] - nodes[i+1])

            if node_diff < difference:
                difference = node_diff

        return difference