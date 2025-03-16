class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time- O(n), Space- O(1)
        # Leetcode-392: https://leetcode.com/problems/is-subsequence/
        # Copy the below code logic
        i, j = 0,0
        if len(s) == j:
            return True
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if len(s) == j:
                return True
        return False