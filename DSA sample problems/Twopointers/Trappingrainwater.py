"""
Leetcode: https://leetcode.com/problems/trapping-rain-water/description/
Intuition: We will use a two-pointer approach. At each step, we will update the maximum and minimum values while traversing the array to effectively calculate the trapped rainwater.

Time complexity: O(n)--We traverse the array once.

Space complexity: O(1)-- We use a constant amount of extra space.

"""
class Solution(object):
    def __init__(self):
        pass
    def trap(self, height: list[int]) -> int:
        i,j = 0,len(height)-1
        min_h, max_h, ans = 0,0,0
        while i < j:
            # calculate min height
            min_h = min(height[i], height[j])
            # calculate curr max height
            max_h = max(min_h, max_h)
            # Add the difference in the ans as we can trap that much water
            ans += (max_h - min_h)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
    
if __name__=="__main__":
    height = [4,2,0,3,2,5]
    ob = Solution()
    print(ob.trap(height))
    