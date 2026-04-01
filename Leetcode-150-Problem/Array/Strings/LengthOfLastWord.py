class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s)-1
        count = 0
        while i >= 0:
            if s[i] != " ":
                count +=1
                i -=1
            else:
                break
        return count