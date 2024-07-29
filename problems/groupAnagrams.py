class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString not in grouped.keys():
                grouped[sortedString] = [string]
            else:
                grouped[sortedString].append(string)
        
        listGrouped = []

        for values in grouped.values():
            listGrouped.append(values)
        
        return listGrouped
                