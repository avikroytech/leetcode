class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                record.append(record[-1]*2)
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))
        
        total = 0
        
        for score in record:
            total += score

        return total