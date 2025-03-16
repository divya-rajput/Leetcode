class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time- O(n), Space- O(n)
        # Leetcode-3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
        # Copy the below code logic
        charSet = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res