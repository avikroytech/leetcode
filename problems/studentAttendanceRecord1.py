class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        consecutiveLates = 0

        for day in s:
            match day:
                case "L":
                    consecutiveLates += 1
                    if consecutiveLates >= 3:
                        return False
                case "A":
                    absent += 1
                    consecutiveLates = 0
                case _:
                    consecutiveLates = 0
        
        return absent < 2 and consecutiveLates < 3