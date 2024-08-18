class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        mapping = {}

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            if char not in mapping.keys():
                if words[i] in mapping.values():
                    return False
                mapping[char] = words[i]
            elif mapping[char] != words[i]:
                return False
        
        return True