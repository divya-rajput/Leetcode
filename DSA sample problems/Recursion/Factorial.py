"""
GeekforGeeks: https://www.geeksforgeeks.org/problems/factorial5739/1
Factorial: 4! = 4*3*2*1 = 24
Base condition: f(1) = 1
Recusrion: f(x) = x * f(x-1)
constraint : 1 < n < 1000
"""
class Solution(object):
    def __init__(self):
        pass
    def factorial(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.factorial(n-1)
    
if __name__=="__main__":
    input1 = 4
    input2 = 10
    input3 = 1
    ob = Solution()
    print(ob.factorial(input1))
    print(ob.factorial(input2))
    print(ob.factorial(input3))

