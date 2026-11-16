class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if not s.isdigit() or k < 2 or k > 100 or len(s)  < 1 or len(s) > 100:
            return ""
        while (len(s) > k):
            new_c = ""
            for i in range(0, len(s), k):
                cut_c = s[i: i + k]
                fc = 0
                for elem in cut_c:
                    fc += int(elem)
                new_c += str(fc)
            s = new_c
        return s
