class Solution:
    def jump(self, nums: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-45: https://leetcode.com/problems/jump-game-ii/
        # Copy the below code logic
        res=0
        l=r=0
        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res