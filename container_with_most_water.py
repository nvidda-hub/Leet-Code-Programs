class Solution:
    def maxArea(self, height) -> int:
        size = len(height)
        start = 0
        end = size - 1
        width = end - start
        max_area = 0
        for i in range(size-1):
            width =  end - start
            if height[start] < height[end]:
                area = height[start]*width
                start = start + 1
            elif height[start] >= height[end]:
                area = height[end]*width
                end = end - 1
            max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))