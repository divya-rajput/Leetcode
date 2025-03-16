class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-169: https://leetcode.com/problems/majority-element/
        # Copy the below code logic
        votes = 0
        candidate = -1
        for i in range (len(nums)):
            if (votes == 0):
                candidate = nums[i]
                votes = 1
            else:
                if (nums[i] == candidate):
                    votes += 1
                else:
                    votes -= 1
        return candidate