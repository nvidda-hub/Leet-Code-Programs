class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400,100, 90, 50, 40, 10, 9, 5, 4,1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while num > 0:
            temp = num // val[i]
            roman_num = roman_num + temp*symbol[i]
            num = num - temp*val[i]
            i = i + 1
        return roman_num


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3999))