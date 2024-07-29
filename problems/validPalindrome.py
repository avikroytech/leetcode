class Solution:
	def isPalindrome(self, s: str) -> bool:
		lower = s.lower()
		words = []
		for char in s.lower():
			if char.isalpha() or char.isdigit():
				words.append(char)
		joinedString = "".join(words)
		reversed_string = joinedString[::-1]
		return joinedString == reversed_string