# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1_number = ""
        list2_number = ""
        isDone = False
        current_node = l1
        while not isDone:
            if not current_node.next:
                isDone = True
                list1_number = list1_number + str(current_node.val)
            else:
                list1_number = list1_number + str(current_node.val)
                current_node = current_node.next
        isDone = False
        current_node = l2
        while not isDone:
            if not current_node.next:
                isDone = True
                list2_number = list2_number + str(current_node.val)
            else:
                list2_number = list2_number + str(current_node.val)
                current_node = current_node.next
        total = str(int(list1_number[::-1]) + int(list2_number[::-1]))
        length = len(total)
        first_node = None
        last_node = None
        for num in total[::-1]:
            if not last_node:
                current_node = ListNode(int(num))
                last_node=current_node
                first_node = current_node
            else:
                current_node = ListNode(num)
                last_node.next = current_node
                last_node = current_node
        return first_node
        