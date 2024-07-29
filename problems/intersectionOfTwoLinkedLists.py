# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        discovered_nodes = []

        current_a = headA
        current_b = headB

        while current_a or current_b:
            if current_a in discovered_nodes:
                return current_a
            elif current_b in discovered_nodes:
                return current_b
            else:
                if current_a:
                    discovered_nodes.append(current_a)
                    current_a = current_a.next
                if current_b:
                    discovered_nodes.append(current_b)
                    current_b = current_b.next

        return None
