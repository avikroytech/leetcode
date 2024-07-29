# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None or head.next == None:
            return head
        
        currentNode = head
        nodes = []

        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next
        
        reversedNodes = nodes[left-1:right]
        reversedNodes.reverse()

        nodes[left-1:right] = reversedNodes

        for i in range(len(nodes)):
            if i != len(nodes)-1:
                nodes[i].next = nodes[i+1]
            else:
                nodes[i].next = None
        
        return nodes[0]
