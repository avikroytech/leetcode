
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        original_list = []
        copy_list = []

        current_node = head

        # Make a deep copy of the list
        while current_node:
            copy_node = Node(current_node.val)
            copy_list.append(copy_node)

            original_list.append(current_node)
            current_node = current_node.next

        # Connect nodes in copied list
        for i in range(len(copy_list)-1):
            copy_list[i].next = copy_list[i+1]

        # Find random node for each node
        for i in range(len(copy_list)):
            original_random = original_list[i].random
            if original_random:
                random_index = original_list.index(original_random)
                copy_list[i].random = copy_list[random_index]

        
        return copy_list[0]