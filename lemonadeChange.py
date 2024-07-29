class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        currentMoney = {
            5: 0,
            10: 0
        }

        for bill in bills:
            if bill == 5:
                currentMoney[5] += 1
            elif bill == 10:
                if currentMoney[5] > 0:
                    currentMoney[5] -= 1
                    currentMoney[10] += 1
                else:
                    return False
            elif bill == 20:
                if currentMoney[5] > 0 and currentMoney[10] > 0:
                    currentMoney[5] -= 1
                    currentMoney[10] -= 1
                elif currentMoney[5] > 2:
                    currentMoney[5] -= 3
                else:
                    return False
        
        return True