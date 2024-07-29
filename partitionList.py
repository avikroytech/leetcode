# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        nodes = []
        currentNode = head
        while currentNode:
            nodes.append(currentNode)
            currentNode = currentNode.next
        
        lessThan = []
        greaterOrEqual = []

        for node in nodes:
            if node.val >= x:
                greaterOrEqual.append(node)
            elif node.val < x:
                lessThan.append(node)
        
        nodes = lessThan + greaterOrEqual

        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]

        return nodes[0]