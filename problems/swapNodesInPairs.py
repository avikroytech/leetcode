# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
            
        currentNode = head
        i = 1
        previousNode = None

        while currentNode.next:
            if (i+1) % 2 == 0:
                if previousNode:
                    previousNext = previousNode.next
                    currentNext = currentNode.next
                    
                    currentNode.next = currentNode.next.next
                    previousNode.next = currentNext
                    previousNode.next.next = previousNext
                    
                    previousNode = previousNode.next
                    i += 1
                else:
                    currentNext = currentNode.next
                    futureNext = currentNode.next.next
                    head = currentNode.next

                    currentNode.next.next = currentNode
                    currentNode.next = futureNext

                    previousNode = head
                    i += 1
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                i += 1


        return head

