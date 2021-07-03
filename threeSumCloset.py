class Solution:
    def threeSumClosest(self, num, target) -> int:
        num.sort()
        min_sum = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                three_sum = num[i] + num[j] + num[k]
                if abs(three_sum - target) < abs(min_sum - target):
                    min_sum = three_sum
                if three_sum == target:
                    return three_sum
                elif three_sum < target:   # means more in negative value so increase index to less negative value
                    j = j + 1
                else:
                    k = k - 1
        return min_sum


if __name__ == '__main__':
    ls = [-1, 2, 1, -4]
    s = Solution()
    print(s.threeSumClosest(ls, 1))
