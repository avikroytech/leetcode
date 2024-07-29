# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        nodes = []
        currentNode = head

        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next

        for i in range(1,len(nodes)):
            insert = nodes.pop(i)
            j = i-1
            insertIndex = i
            while j >= 0:
                if nodes[j].val > insert.val:
                    insertIndex = j
                j -= 1
            nodes.insert(insertIndex, insert)
        
        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]

        return nodes[0]