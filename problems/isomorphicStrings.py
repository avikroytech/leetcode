class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}

        for i in range(len(t)):
            if s[i] not in mappings.keys():
                if t[i] in mappings.values():
                    return False
                mappings[s[i]] = t[i]
            else:
                if mappings[s[i]] != t[i]:
                    return False
        
        return True