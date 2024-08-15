class Solution:
    def countSeniors(self, details: list[str]) -> int:
        senior_count = 0

        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                senior_count += 1
        
        return senior_count