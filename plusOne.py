class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        list_of_strings = [str(element) for element in digits]
        number = int("".join(list_of_strings))
        number += 1
        list_of_numbers = [int(element) for element in str(number)]
        return list_of_numbers