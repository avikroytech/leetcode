# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        currentNode = head
        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next
        
        del nodes[len(nodes)-n]

        if len(nodes) < 1:
            return None

        for i in range(len(nodes)):
            if i == len(nodes)-1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        
        return nodes[0]
        

        
