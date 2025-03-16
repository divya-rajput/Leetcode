class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
            # Time- O(n), Space- O(n)
            # Leetcode-128: https://leetcode.com/problems/longest-consecutive-sequence/
            # Copy the below code logic
            longest = 0
            num_set = set(nums)

            for n in num_set:
                if (n-1) not in num_set:
                    length = 1
                    while (n+length) in num_set:
                        length += 1
                    longest = max(longest, length)
            
            return longest
            