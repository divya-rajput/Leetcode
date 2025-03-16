class Solution:
    def isHappy(self, n: int) -> bool:
        # Time- O(n), Space- O(n)
        # Leetcode-202: https://leetcode.com/problems/happy-number/
        # Copy the below code logic
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self.checkSum(n)
        return n == 1

    def checkSum(self, n: int) -> int:
        sum = 0
        while n >= 1:
            i = n %10
            sum += i * i
            n = n // 10
        return sum
        