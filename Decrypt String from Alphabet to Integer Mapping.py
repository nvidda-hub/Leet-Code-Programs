import string


class Solution:
    def freqAlphabets(self, s: str) -> str:
        str1 = ''
        alpha = list(''.join(string.ascii_lowercase))
        i = 0
        count = 0
        while i < len(s) - 2:
            if s[i + 2] != '#':
                str1 = str1 + alpha[int(s[i]) - 1]
                i = i + 1
            else:
                str1 = str1 + alpha[int(s[i:i + 2]) - 1]
                i = i + 3
            print(i)
        for j in range(i, len(s), 1):
            str1 = str1 + alpha[int(s[j]) - 1]
        return str1


new = Solution()
print(new.freqAlphabets("10#11#12"))