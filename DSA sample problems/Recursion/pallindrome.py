"""
Leetcode-125: https://leetcode.com/problems/valid-palindrome/description/
Pallindrome: The string is said to be pallindrome of itself, means the reverese is same as the string.
2 pointer apporach in recursion.
Base condition: if left > right then return true
"""
class Solution(object):
    def __init__(self):
        pass
    def pallindrome(self, st: str, l: int, r: int)-> bool:
        if l > r:
            return True
        return st[l] == st[r] and self.pallindrome(st,l+1,r-1)
    
if __name__ == "__main__":
    ob = Solution()
    st = "abccba"
    if ob.pallindrome(st, 0, len(st)-1):
        print(f"The string {st} is a palindrome")
    else:
        print(f"The string {st} is NOT a palindrome")