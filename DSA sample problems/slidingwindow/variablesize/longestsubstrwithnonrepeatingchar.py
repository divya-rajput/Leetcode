"""
Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Approach
Use a sliding window with a hash set, using left and right pointers to move the window. 
If the set doesn't contain a character, then first add it into the set and calculate the maxLength hand-in-hand. 
If a character is already present in the set, that means you have to move your sliding window by 1. 
Before that, you have to remove all the characters that are in front of the character that is already present in the window. 
Now, you have to remove that character as well, move the left pointer, and add the new character into the set. 

Complexity
Time complexity: O(n)
Space complexity: O(k), where k is the number of distinctive characters prsent in the hashset.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        start, end = 0,0
        ans_idx, ans_len = 0, 0
        while end < len(s):
            while s[end] in res:
                res.remove(s[start])
                start += 1
            res.add(s[end])
            end += 1
            if(ans_len < len(res)):
                ans_len = len(res)
                ans_idx = start
        return s[ans_idx:ans_len+ans_idx], ans_len
        
    
if __name__ == "__main__":
    ob = Solution()
    st1 = "abcabcbb"
    st2 = "bbbbb"
    st3 = "pwwkew"
    print(ob.lengthOfLongestSubstring(st1))
    print(ob.lengthOfLongestSubstring(st2))
    print(ob.lengthOfLongestSubstring(st3))