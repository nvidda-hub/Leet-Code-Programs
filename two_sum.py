class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        num_dict = {item: idx for idx, item in enumerate(nums) if item < target}
        nums = dict(sorted(num_dict.items(), key=lambda x: x[0]))
        needed = []
        for k, v in nums.items():
            temp = target - k
            if temp in nums.keys():
                needed.append(nums[k])
                needed.append(nums[temp])
                break
        return needed


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([15, 20, 6, 3, 1, 2, 8, 25], 45))