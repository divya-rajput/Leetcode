class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-27: https://leetcode.com/problems/remove-element/
        # Copy the below code logic
        while val in nums:
            nums.remove(val)
        return len(nums)