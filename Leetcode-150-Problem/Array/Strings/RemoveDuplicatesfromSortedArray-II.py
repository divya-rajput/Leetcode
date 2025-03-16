class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-80: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
        # Copy the below code logic
        l,r = 0,0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            for i in range(min(2,count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l