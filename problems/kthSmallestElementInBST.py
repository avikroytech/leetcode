# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        queue = [root]
        treeVals = []
        
        while(len(queue) > 0):

            # remove front from queue
            node = queue.pop(0)
            treeVals.append(node.val)

            # Enqueue left child
            if node.left:
                queue.append(node.left)

            # Enqueue right child
            if node.right:
                queue.append(node.right)
        
        treeVals = sorted(treeVals)

        return treeVals[k-1]