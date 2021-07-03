class Solution:
    def sortString(self, s: str) -> str:

        ls = []
        for c in s:
            ls.append(ord(c))
        count = 0
        index = sorted(ls)
        result = chr(index[0])
        min1 = index[0]
        max1 = index[len(index) - 1]
        for i in range(len(index)):
            if index[i] > min1 and index[i] < max1:
                result = result + chr(index[i])
            elif index[i] < max1 and index[i] != min1:
                result = result + chr(index[i])
            elif count == 0 and index[i] == max1:
                result = result + chr(index[i])
                count = count + 1
        return result