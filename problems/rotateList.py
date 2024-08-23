# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        nodes = []
        currentNode = head
        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next

        nodes[:] = nodes[len(nodes)-k%len(nodes):] + nodes[:len(nodes)-k%len(nodes)]

        for i in range(len(nodes)):
            if i == len(nodes)-1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        
        return nodes[0]