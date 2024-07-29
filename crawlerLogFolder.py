class Solution:
    def minOperations(self, logs: list[str]) -> int:
        operations_needed = 0
        for log in logs:
            match log:
                case '../':
                    if operations_needed > 0:
                        operations_needed -= 1
                case './':
                    continue
                case _:
                    operations_needed += 1
        
        return operations_needed