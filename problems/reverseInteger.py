class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        x_list = []
        for num in str(x):
            if num == "-":
                negative = True
                num = ""
            x_list.append(num)
        absolute_x = "".join(x_list)
        if negative:
            reversed_x = int("-" + absolute_x[::-1])
        else:
            reversed_x = int(str(x)[::-1])
        if reversed_x < -2**31 or reversed_x > 2**31-1:
            return 0
        return reversed_x
