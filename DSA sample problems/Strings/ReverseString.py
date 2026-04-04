class Solution:
    def reverseString(self, s: list[str]) -> None:
        #Problem: https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=string
        """
        Do not return anything, modify s in-place instead.
        """
        i , j = 0, len(s) -1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        