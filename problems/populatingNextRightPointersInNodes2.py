# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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

    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        nodes = self.traverseTree(root, [[]], 0)

        for row in nodes:
            for i in range(len(row)-1):
                row[i].next = row[i+1]

        return root