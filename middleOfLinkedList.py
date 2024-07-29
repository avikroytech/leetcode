# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodes = 0
        currentNode = head
        middle = head

        while currentNode:
            nodes += 1
            if nodes % 2 == 0:
                middle = middle.next
            currentNode = currentNode.next
        
        return middle