class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        forged_note = []
        letters_left = list(ransomNote)

        for current_letter in magazine:
            if current_letter in letters_left:
                forged_note.append(current_letter)
                letters_left.remove(current_letter)
        
        return sorted(forged_note) == sorted(list(ransomNote))
