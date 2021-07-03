class Solution(object):
    def myAtoi(self, s)-> int:
        ans = ""
        s = s.lstrip()
        if not s or (not s[0].isnumeric() and s[0]!= '-' and s[0]!= '+'):
            return 0

        if s[0].isalpha():
            return 0
        else:
            ans = ans + s[0]
            for i in range(1,len(s)):
                if not s[i].isnumeric():
                    break
                ans = ans + s[i]
        if ans == '-' or ans == '+':
            return 0
        else:
            ans = int(ans)
            if ans < -2**31:
                ans = -2**31
            elif ans > 2**31 - 1:
                ans = 2**31 - 1

            return ans

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("  0032"))