# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        mergedList = []
        if list1:
            currentNode = list1
            while currentNode:
                mergedList.append(currentNode.val)
                currentNode = currentNode.next
        
        if list2:
            currentNode = list2
            while currentNode:
                mergedList.append(currentNode.val)
                currentNode = currentNode.next

        mergedList.sort()
        
        for i in range(len(mergedList)):
            mergedList[i] = ListNode(mergedList[i])

        for i in range(len(mergedList)):
            if i < len(mergedList) - 1:
                mergedList[i].next = mergedList[i+1]
        
        if len(mergedList) > 0:
            return mergedList[0]
        else:
            return None