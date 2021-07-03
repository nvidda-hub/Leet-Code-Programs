class Solution:
    def minCostToMoveChips(self, position):
        cost = 0
        count = []

        temp = []
        for num in position:
            count.append(position.count(num))
            temp.append(num)

        e_c = 0  # even_counter
        o_c = 0  # odd_counter
        for ele in set(position):
            if ele % 2 == 0:
                e_c += 1
            else:
                o_c += 1
        ls_final = sorted(set(zip(count, temp)), reverse=True)

        if e_c > o_c:
            for i in range(len(ls_final)):
                if ls_final[i][1] % 2 != 0:
                    cost = cost + ls_final[i][0]
        elif e_c < o_c:
            for i in range(len(ls_final)):
                if ls_final[i][1] % 2 == 0:
                    cost = cost + ls_final[i][0]
        else:
            initial = ls_final[0][1]
            for i in range(1, len(ls_final)):
                if abs(ls_final[i][1] - initial) % 2 != 0:
                     cost = cost + ls_final[i][0]
        return cost


s1 = Solution()
print(s1.minCostToMoveChips([1, 2, 3]))
