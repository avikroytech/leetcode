# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current_node = head
        nodes = []

        index = 1

        while current_node:
            nodes.append(current_node)

            current_node = current_node.next

        i = 0
        while i < len(nodes):
            reversed_group = nodes[i:i+k]
            if len(reversed_group) == k:
                reversed_group = reversed_group[::-1]
                nodes[i:i+k] = reversed_group
                i += k
            else:
                break

        
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[-1].next = None

        return nodes[0]