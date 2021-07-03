from numpy import zeros as zs


class Solution:
    def oddCells(self, n, m, indices):
        mat = zs(shape=(n, m), dtype=int)
        for item in indices:
            j = 0
            while j <= m - 1:
                mat[item[0]][j] = mat[item[0]][j] + 1
                j = j + 1
            j = 0

            while j <= n - 1:
                mat[j][item[1]] = mat[j][item[1]] + 1
                j = j + 1
        return len(mat[mat % 2 != 0])


s1 = Solution()
print(s1.oddCells(2, 2, [[1,1],[0,0]]))