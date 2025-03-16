class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time- O(n), Space- O(n)
        # Leetcode-1: https://leetcode.com/problems/two-sum/
        # Copy the below code logic
        
        secondNumList = {}
        for i in range(len(nums)):
            secondNum = target - nums[i]
            print("Nums=",secondNum)
            if secondNum in secondNumList:
                return [i,secondNumList[secondNum]]   
            else:
                secondNumList[nums[i]] = i

        # Solution-2 Only works when sorting is applied(if allowed)
        # Time- O(nlogn), Space- O(1)
        # Leetcode-1: https://leetcode.com/problems/two-sum/
        # Copy the below code logic
        nums.sort()
        print(nums)
        l,r = 0, len(nums) -1
        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l, r]