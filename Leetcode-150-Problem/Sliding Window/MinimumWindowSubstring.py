class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time- O(n), Space- O(1)
        # Leetcode-76: https://leetcode.com/problems/minimum-window-substring/
        # Copy the below code logic
        newStr = set()
        currentCount = 0
        maxCount = 0
        for ch in s:
            if ch not in newStr:
                currentCount +=1
                newStr.add(ch)
            else:
                if currentCount > maxCount:
                    maxCount = currentCount
                    currentCount = 1
        return maxCount