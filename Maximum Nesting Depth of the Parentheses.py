class Solution:
    def maxDepth(self, s: str) -> int:
        s = list(filter(lambda x: x == ")" or x == "(", list(s)))
        best = 0
        p_count = 0
        for i in range(len(s)):
            if s[i] == "(":
                p_count += 1
                best = max(best, p_count)
            else:
                p_count -= 1
        return (best)

s1 = Solution()
print(s1.maxDepth("(1+(2*3)+((8)/4))+1"))
