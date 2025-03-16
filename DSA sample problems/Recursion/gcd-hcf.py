"""
Leetcode-1979: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
GCD/HCF: Two nums are 16 and 24
16 = 2*2*2*2
24 = 2*2*2*3
Pick common digits and multiplication of those common didgit is the answer, here it will be 8
Other approach
Let take the example of 16 and 24
minimum of two will be the divisor, lets say a
the other will be divident, lets say b
Base condition: if b == 0 then return a
Recusrion: gcd(b, a%b)
constraint : 1 < n < 1000
"""
class Solution(object):
    def __init__(self):
        pass
    def gcd_hcf(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd_hcf(b, a%b)
    
if __name__=="__main__":
    input1 = 28
    input2 = 48
    ob = Solution()
    print(ob.gcd_hcf(max(input1, input2), min(input1, input2)))