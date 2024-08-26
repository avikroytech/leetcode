# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, node):
        if not node:
            return 0
        else:
            leftHeight = self.getHeight(node.left)
            rightHeight = self.getHeight(node.right)
            if leftHeight > rightHeight:
                return leftHeight+1
            else:
                return rightHeight+1


    def traverseTree(self, node, levelIndex):
        if not node:
            return []
        if levelIndex == 1:
            return [node.val]
        elif levelIndex > 1:
            level = []
            level += self.traverseTree(node.left, levelIndex-1)
            level += self.traverseTree(node.right, levelIndex-1)

            return level


    def averageOfLevels(self, root: TreeNode) -> list[float]:
        height = self.getHeight(root)
        averages = []

        for i in range(1, height+1):
            level = self.traverseTree(root, i)

            averages.append(sum(level) / len(level))

        return averages
