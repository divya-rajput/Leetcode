class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Time- O(n), Space- O(n)
        # Leetcode-219: https://leetcode.com/problems/contains-duplicate-ii/
        # Copy the below code logic
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if abs(i-dic[nums[i]]) <= k:
                    return True
                dic[nums[i]] = i
        return False      