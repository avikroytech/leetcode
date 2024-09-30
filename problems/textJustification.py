import math

class Solution:
    def formatRow(self, row, maxWidth):
        spaces_left = maxWidth - len("".join(row))

        if len(row) == 1:
            formatted_row = row[0] + " " * spaces_left
            return formatted_row

        formatted_row = ""
        num_spaces = math.ceil(spaces_left / (len(row) - 1))

        for i in range(len(row) - 1):
            word = row[i]
            if spaces_left - num_spaces < 0:
                num_spaces -= 1
            elif spaces_left - num_spaces <= 0 and i != len(row)-2:
                num_spaces -= 1

            formatted_row += word + " " * num_spaces
            spaces_left -= num_spaces

        formatted_row += row[-1]

        return formatted_row

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        justified_text = []
        current_length = 0
        row = []

        while len(words) > 0:
            word = words[0]
            # print(word)

            if (
                len(word) + current_length == maxWidth
                or len(word) + 1 + current_length == maxWidth
            ):
                row.append(word)
                current_length = 0
                formatted_row = self.formatRow(row, maxWidth)
                justified_text.append(formatted_row)
                row = []
                words.pop(0)
            elif len(word) + 1 + current_length < maxWidth:
                row.append(word)
                current_length += len(word) + 1
                words.pop(0)
            else:
                formatted_row = self.formatRow(row, maxWidth)
                justified_text.append(formatted_row)
                row = []
                current_length = 0

        if len(row) > 0:
            formatted_row = " ".join(row)
            formatted_row += " " * (maxWidth - len(formatted_row))
            justified_text.append(formatted_row)

        return justified_text
