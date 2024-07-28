class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for string in strs:
            if prefix == "":
                break
            newprefix = ""
            for i in range(len(string)):
                if i == len(prefix):
                    break
                elif string[i] == prefix[i]:
                    newprefix += string[i]
                else:
                    break
            prefix = newprefix
        return prefix