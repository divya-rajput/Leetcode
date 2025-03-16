class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-11: https://leetcode.com/problems/container-with-most-water/
        # Copy the below code logic
        l = 0
        r = len(height)-1
        arealist = []
        while l != r :
            area = (r-l)*min(height[l] , height[r])
            arealist.append(area)
            if height[l] < height [r]:
                l += 1
            else:
                r += -1
        return max(arealist)