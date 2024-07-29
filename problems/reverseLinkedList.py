# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = []
        currentNode = head
        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next

        nodes.reverse()

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[-1].next = None
        
        return nodes[0]