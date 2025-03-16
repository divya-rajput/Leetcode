"""
Leetcode-509: https://leetcode.com/problems/fibonacci-number/description/
Fibonacci:  0 1 1 2 3 5 8 13 21 34 55
Base condition: f(1) = 1 and f(0) = 0
Recusrion: f(x) = f(x-1) + f(x-2)
constraint : 0 < n < 1000
"""
class Solution(object):
    def __init__(self):
        pass
    def fibonacci(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    
if __name__=="__main__":
    input1 = 4
    input2 = 10
    input3 = 1
    ob = Solution()
    print(ob.fibonacci(input1))
    print(ob.fibonacci(input2))
    print(ob.fibonacci(input3))