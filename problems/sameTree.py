# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeTraversal(self, node):
        nodes = [node.val]
        print(f"Node: {node.val} -- Left: {node.left.val if node.left else node.left} Right: {node.right.val if node.right else node.right}")

        if node.left:
            result = self.treeTraversal(node.left)
            nodes = result + nodes
        else:
            nodes = [None] + nodes
        if node.right:
            result = self.treeTraversal(node.right)
            nodes += result
        else:
            nodes += [None]

        return nodes


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        # Create an empty queue
        # for level order traversal
        pTreeQueue = [p]
        qTreeQueue = [q]

        # Track nodes in both trees
        pTracked = []
        qTracked = []

        # Traverse through queue for p
        while(len(pTreeQueue) > 0):

            # remove front from queue
            node = pTreeQueue.pop(0)
            if node:
                pTracked.append(node.val)

                # Enqueue left child
                pTreeQueue.append(node.left)

                # Enqueue right child
                pTreeQueue.append(node.right)
            else:
                pTracked.append(node)

        # Traverse through queue for q
        while(len(qTreeQueue) > 0):

            # remove front from queue
            node = qTreeQueue.pop(0)
            if node:
                qTracked.append(node.val)

                # Enqueue left child
                qTreeQueue.append(node.left)

                # Enqueue right child
                qTreeQueue.append(node.right)
            else:
                qTracked.append(node)

        return pTracked == qTracked