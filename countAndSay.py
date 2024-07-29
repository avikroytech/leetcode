def recursiveCount(n, number, say):
    if number == n:
        return say

    stack = ""
    returnSay = ""

    for i in say:
        if i not in stack and len(stack) > 0:
            returnSay += str(len(stack)) + stack[0]
            stack = i
        else:
            stack += i

    if len(stack) > 0:     
        returnSay += str(len(stack)) + stack[0]


    return recursiveCount(n, number+1, returnSay)

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = recursiveCount(n, 1, "1")

        return result
        
