# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, node, nodes, level):
        if len(nodes) - 1 < level:
            nodes.append([])

        nodes[level].append(node)

        if node.left:
            nodes = self.traverseTree(node.left, nodes, level+1)
        if node.right:
            nodes = self.traverseTree(node.right, nodes, level+1)

        return nodes

    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return root
        
        nodes = self.traverseTree(root, [[]], 0)
        rightSideNodes = []

        for row in nodes:
            rightSideNodes.append(row[-1].val)

        return rightSideNodes