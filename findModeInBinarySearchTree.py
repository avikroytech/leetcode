# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def traverseTree(self, node):
        count = {node.val: 1}
        left = None
        right = None

        if not node.left and not node.right:
            return count
        
        if node.left:
            left = self.traverseTree(node.left)
        if node.right:
            right = self.traverseTree(node.right)

        if left:
            for i in left.keys():
                if i in count.keys():
                    count[i] += left[i]
                else:
                    count[i] = left[i]
        if right:
            for i in right.keys():
                if i in count.keys():
                    count[i] += right[i]
                else:
                    count[i] = right[i]

        return count

    def findMode(self, root: TreeNode) -> list[int]:
        count = self.traverseTree(root)
        modes = [root.val]

        for val in count.keys():
            if count[val] > count[modes[0]]:
                modes = [val]
            elif count[val] == count[modes[0]] and val not in modes:
                modes.append(val)
        
        return modes