class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        results = []

        for num in range(left, right+1):
            if "0" not in str(num):
                selfDividing = True
                for digit in str(num):
                    if num % int(digit) != 0:
                        selfDividing = False
                
                if selfDividing:
                    results.append(num)
        
        return results