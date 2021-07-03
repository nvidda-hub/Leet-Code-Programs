class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        if numRows == 1 or len(s) <= 2:
            return s
        else:
            for i in range(numRows):
                if i == 0 or i == numRows-1:
                    k = 2*(numRows - 1)
                    j = 0
                    while (i+j*k) < len(s):
                        ans = ans + s[i+(j*k)]
                        print(f"i : {i} and jk : {i+j*k}")
                        j = j + 1
                elif 0 < i < numRows-1:
                    j = i
                    k1 = j
                    k2 = j + 2*(numRows - (i+1))
                    while k1 <= len(s)-1:
                        if k2 <= len(s)-1:
                            print(f"i : {i} and k1 : {k1}, k2 : {k2}")
                            ans = ans + s[k1] + s[k2]
                            k1 = k2 + 2*i
                            k2 = k1 + 2*(numRows - (i+1))
                        elif k1 <= len(s)-1 < k2:
                            print(f"k1 : {k1}")
                            ans = ans + s[k1]
                            print(f"ans : {ans}")
                            break

            return ans


if __name__ == '__main__':
    s = "ABCD"
    s1 = Solution()
    print(s1.convert(s, 3))

    # PAYPALISHIRING
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
