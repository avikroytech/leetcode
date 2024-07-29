# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        values = []
        current_node = head
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next
        i = 0
        while i < len(values)-1:
            if values[i] == values[i+1]:
                values.pop(i)
            else:
                i += 1

        print(values)
        if len(values) == 0:
            return None
        nodes = []

        for val in values:
            nodes.append(ListNode(val))

        n = 0
        while n < len(nodes)-1:
            nodes[n].next = nodes[n+1]
            n += 1

        return nodes[0]
        