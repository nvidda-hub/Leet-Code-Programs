class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        str1 = ''
        for c in S:
            if c is '(' and count == 0:
                count = count + 1
            elif c is ')' and count == 1:
                count = count - 1
            else:
                if c is '(':
                    count = count + 1
                elif c is ')':
                    count = count - 1

                str1 = str1 + c
        return str1
