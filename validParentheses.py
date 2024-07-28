class Solution:
	def isValid(self, s: str) -> bool:
		parenthesesMatch = []
		for char in s:
			if char in "({[":
				parenthesesMatch.append(char)
			else:
				if len(parenthesesMatch) == 0 or \
					(char == ")" and parenthesesMatch[-1] != "(") or \
					(char == "]" and parenthesesMatch[-1] != "[") or \
					(char == "}" and parenthesesMatch[-1] != "{"):
					return False
				parenthesesMatch.pop()
		
		return not parenthesesMatch