# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		pos = 0
		current_node = head
		nodes = []

		while current_node:
			nodes.append(current_node)
			if current_node.next in nodes:
				return True
			current_node = current_node.next

		return False