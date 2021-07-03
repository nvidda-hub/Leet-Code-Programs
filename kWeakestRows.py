class Solution:
    def kWeakestRows(self, mat, k: int):
        d = {}
        for i in range(len(mat)):
            d[i] = sum(mat[i])

        arr = sorted(d, key=d.get)
        return arr[:k]


s1 = Solution()
print(s1.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))