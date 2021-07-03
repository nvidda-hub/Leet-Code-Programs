class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while True:
            try:
                if p[-1] == "*":
                    while p[-2:] == p[-4:-2]:
                        p = p[:-2]
                    if self.isMatch(s, p[:-2]):
                        return True
                    elif p[-2] in [s[-1],"."]:
                        s = s[:-1]
                    else:
                        return False
                else:
                    if p[-1] in [s[-1], "."]:
                        s = s[:-1]
                        p = p[:-1]
                    else:
                        return False
            except:
                return not s and not p


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("mississippi", "mis*is*p*."))