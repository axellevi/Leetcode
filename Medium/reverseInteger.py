class Solution:
    def reverse(self, x: int) -> int:
        inverse = 0
        if x >= 0:
            y = 1
        else:
            x = -x
            y = -1
        while (x > 0):
            last = x % 10
            inverse = (inverse * 10) + last
            x = x // 10
        if -2**31 >= inverse or inverse >= 2**31 - 1:
            return 0
        return inverse * y