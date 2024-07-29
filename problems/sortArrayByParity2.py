class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        answer = []

        for i in range(len(odd)):
            answer.append(even[i])
            answer.append(odd[i])
        
        return answer