# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        currentHead = head
        previousNode = head
        currentNode = head
        while currentNode:
            if currentNode.val == val and currentNode == currentHead:
                currentHead = currentNode.next
            elif currentNode.val == val:
                previousNode.next = currentNode.next
            else:
                previousNode = currentNode
            currentNode = currentNode.next
        
        return currentHead