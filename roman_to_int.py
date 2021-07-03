class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,  'X': 10, 'V': 5, 'I': 1}
        ans = 0
        prev = None
        for c in s:
            if prev and romans[prev] < romans[c]:
                ans = ans + (romans[c]-(romans[prev]*2))
            else:
                ans = ans + romans[c]
            prev = c
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("IV"))