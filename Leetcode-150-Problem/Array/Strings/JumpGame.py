class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Time- O(n), Space- O(1)
        # Leetcode-55: https://leetcode.com/problems/jump-game/
        # Copy the below code logic
        lastgoodposition=len(nums)-1

        for i in range(len(nums)-1,-1,-1):

            if i+nums[i]>=lastgoodposition:
                lastgoodposition=i


        return lastgoodposition==0