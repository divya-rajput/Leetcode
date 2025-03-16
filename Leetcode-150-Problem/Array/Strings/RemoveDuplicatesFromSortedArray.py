class Solution:
    def removeDuplicates(self, x: list[int]) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        # Copy the below code logic
        i = 0
        for j in range(1, len(x)):
            if x[i] != x[j]:
                i += 1
                x[i], x[j] = x[j], x[i]
        return i+1
        