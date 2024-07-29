class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    stack.append(str(operand1 + operand2))
                case "-":
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())
                    stack.append(str(operand1 - operand2))
                case "*":
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    stack.append(str(operand1 * operand2))
                case "/":
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())
                    result = int(operand1 / operand2)
                    stack.append(str(result))
                case _:
                    stack.append(token)
        
        return int(stack[0])