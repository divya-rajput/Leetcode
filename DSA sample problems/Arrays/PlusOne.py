class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Problem: https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array
        for  i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1]+ digits