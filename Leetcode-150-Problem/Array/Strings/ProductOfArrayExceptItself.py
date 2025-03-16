class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time- O(n), Space- O(1)
        # Leetcode-238: https://leetcode.com/problems/product-of-array-except-self/
        # Copy the below code logic
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result