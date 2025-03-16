'''
    Leetcode-231---> Power of Two
    Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2^x.
    Example 1:
    Input: n = 1
    Output: true
    Explanation: 20 = 1   
'''
#Copy the below code in Leetcode

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n<=0 or n%2 != 0:
            return False
        return self.isPowerOfFour(n/2)
    
# if __name__ == "__main__":
#     obj = Solution()
#     print(obj.isPowerOfFour(16))
#     print(obj.isPowerOfFour(9))