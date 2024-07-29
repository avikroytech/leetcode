# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        currentNode = head
        marked = None
        while currentNode and currentNode.next:
            currentNode.val = marked
            if currentNode.next.val != marked:
                currentNode = currentNode.next
            else:
                return currentNode.next
        return None