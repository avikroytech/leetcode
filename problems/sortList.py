# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        currentNode = head
        values = []
        while currentNode:
            values.append(currentNode.val)
            currentNode = currentNode.next

        values.sort()

        for i in range(len(values)):
            values[i] = ListNode(values[i])
        
        for i in range(len(values)-1):
            values[i].next = values[i+1]
        
        return values[0]