# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node, path):
        if not node.left and not node.right:
            return [path + str(node.val)]

        
        path = path + str(node.val)
        leafDigits = []

        if node.left:
            leftDigits = self.traverseTree(node.left, path)
            for digit in leftDigits:
                leafDigits.append(digit)
        if node.right:
            rightDigits = self.traverseTree(node.right, path)
            for digit in rightDigits:
                leafDigits.append(digit)
        
        return leafDigits
        

    def sumNumbers(self, root: TreeNode) -> int:
        results = self.traverseTree(root, '')
        path_sum = 0

        for result in results:
            path_sum += int(result)

        return path_sum