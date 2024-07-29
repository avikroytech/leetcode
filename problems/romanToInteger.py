class Solution:
    def romanToInt(self, s: str) -> int:
        converted_int = 0
        index = 0
        isTwoNumerals = False
        for letter in s:
            match letter:
                case "I":
                    if not index == len(s) - 1:
                        if s[index+1] == "V":
                            converted_int += 4
                            isTwoNumerals = True
                        elif s[index+1] == "X":
                            converted_int += 9
                            isTwoNumerals = True
                        else:
                            converted_int += 1
                    else:
                        converted_int += 1
                case "V":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    else:
                        converted_int += 5
                case "X":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    elif not index == len(s) - 1:
                        if s[index+1] == "L":
                            converted_int += 40
                            isTwoNumerals = True
                        elif s[index+1] == "C":
                            converted_int += 90
                            isTwoNumerals = True
                        else:
                            converted_int += 10
                    else:
                        converted_int += 10
                case "L":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    else:
                        converted_int += 50
                case "C":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    elif not index == len(s) - 1:
                        if s[index+1] == "D":
                            converted_int += 400
                            isTwoNumerals = True
                        elif s[index+1] == "M":
                            converted_int += 900
                            isTwoNumerals = True
                        else:
                            converted_int += 100
                    else:
                        converted_int += 100
                case "D":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    else:
                        converted_int += 500
                case "M":
                    if isTwoNumerals:
                        isTwoNumerals = False
                    else:
                        converted_int += 1000
            index += 1
            

        return converted_int