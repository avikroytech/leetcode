# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root is None:
            return result

        # Create an empty queue for level order traversal
        q = [root]

        while q:
        
            # nodeCount (queue size) indicates number 
            # of nodes at current level.
            nodeCount = len(q)
            currentLevel = []

            for i in range(nodeCount):
                node = q.pop(0)
                currentLevel.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            result.append(currentLevel)

        return result[::-1]