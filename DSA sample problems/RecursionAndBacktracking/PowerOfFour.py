'''
    Leetcode-342---> Power of Four
    Given an integer n, return true if it is a power of four. Otherwise, return false.
    An integer n is a power of four, if there exists an integer x such that n == 4^x.
    Example 1:
    Input: n = 16
    Output: true
 
'''
#Copy the below code in Leetcode

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n<=0 or n%4 != 0:
            return False
        return self.isPowerOfFour(n/4)
    
# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.isPowerOfFour(16))