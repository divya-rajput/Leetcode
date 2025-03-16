'''
    Leetcode-326---> Power of Three
    Given an integer n, return true if it is a power of three. Otherwise, return false.
    An integer n is a power of three, if there exists an integer x such that n == 3^x.
    Example 1:
    Input: n = 27
    Output: true
    Explanation: 27 = 33 
'''
#Copy the below code in Leetcode

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n<=0 or n%3 != 0:
            return False
        return self.isPowerOfFour(n/3)
    
# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.isPowerOfFour(16))
#     print(obj.isPowerOfFour(9))