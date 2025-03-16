class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Time- O(n), Space- O(1)
        # Leetcode-167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
        # Copy the below code logic
        left, right = 0, len(numbers) -1
        while left < right:
            newNum = numbers[left] + numbers[right]
            if newNum > target:
                right -= 1
            elif newNum < target:
                left += 1
            else:
                return [left+1,right+1]