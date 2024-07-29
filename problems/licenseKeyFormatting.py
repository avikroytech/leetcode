class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key = ''.join(s.upper().split('-'))
        reformatted = ''

        if len(key) % k != 0:
            firstGroup = len(key) % k
            reformatted = key[:firstGroup]
            key = key[firstGroup:]
        
        group = ''

        for char in key:
            if len(group) < k:
                group += char
            else:
                if len(reformatted) > 0:
                    reformatted += '-' + group
                else:
                    reformatted = group
                
                group = char
        
        if len(group) > 0:
            if len(reformatted) > 0:
                reformatted += '-' + group
            else:
                reformatted = group
        
        return reformatted
