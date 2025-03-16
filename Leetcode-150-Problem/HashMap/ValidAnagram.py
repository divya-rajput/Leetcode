class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time- O(n), Space- O(n)
        # Leetcode-242: https://leetcode.com/problems/valid-anagram/
        # Copy the below code logic
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
            if d[char] == 0:
                del d[char]
        return True if len(d) == 0 else False