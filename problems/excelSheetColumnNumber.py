class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        col_num = 0

        for i in range(len(columnTitle)):
            col = columnTitle[len(columnTitle)-1-i]

            val = (alphabet.index(col) + 1)  * 26**i
            col_num += val

        return col_num