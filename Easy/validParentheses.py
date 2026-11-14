class Solution:
    def isValid(self, s: str) -> bool:
        inverse = {'}':'{', ')':'(', ']':'['}
        ouvrant = {'{', '(', ('[')}
        stack = []

        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in ouvrant:
                stack.append(s[i])
            else:
                if inverse[s[i]] not in stack or inverse[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True