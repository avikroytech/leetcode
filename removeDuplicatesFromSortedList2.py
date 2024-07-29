# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        duplicates = []
        currentNode = head

        if not head or not head.next:
            return head

        while currentNode:
            if currentNode.next:
                if currentNode.val == currentNode.next.val:
                    if currentNode.val not in duplicates:
                        duplicates.append(currentNode.val)
            currentNode = currentNode.next
        
        newNodes = []
        currentNode = head

        while currentNode:
            if currentNode.val not in duplicates:
                newNodes.append(currentNode)
            currentNode = currentNode.next
        
        if len(newNodes) == 1:
            newNodes[0].next = None
            return newNodes[0]
        elif len(newNodes) == 0:
            return None
        
        for i in range(len(newNodes)-1):
            newNodes[i].next = newNodes[i+1]
        
        newNodes[len(newNodes)-1].next = None

        return newNodes[0]