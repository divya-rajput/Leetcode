class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time- O(n), Space- O(n)
        # Leetcode-290: https://leetcode.com/problems/word-pattern/
        # Copy the below code logic
        d ={}
        e = {}
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        for ch,st in zip(pattern, s):
            if ch not in d:
                d[ch] = st
            if st not in e:
                e[st] = ch
            if d[ch] != st or e[st] != ch:
                return False
        return True
        