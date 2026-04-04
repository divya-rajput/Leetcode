class Solution:
    # Problem: https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=string
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for i,ch in enumerate(s):
            if ch in dic and dic[ch] == 1:
                return i
        return -1
