class Solution(object):
    def __init__(self):
        pass
    def reverse(self, n: int)-> int:
        if n == 1:
            return 1
        ans = n + self.reverse(n-1)
        return ans
    
if __name__ == "__main__":
    ob = Solution()
    n = 5
    print(ob.reverse(n))