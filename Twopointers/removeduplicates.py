"""
Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Intuition: If an array is sorted and the immediate next element is the same as the current element, we need to remove the duplicate element.

Time complexity: O(n)-- We traverse the array once.

Space complexity: O(1)--We use a constant amount of extra space.

This approach essentially involves iterating through the array once and removing duplicates in place, which keeps the space complexity minimal.
"""
class Solution(object):
    def __init__(self):
        pass
    def remove_duplicate(self, arr: list[int]) -> int:
        if len(arr) <= 1:
            return arr
        i, j = 1, 1
        while j < len(arr):
            if arr[j] != arr[i-1]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j+= 1
        return i    
    
if __name__=="__main__":
    arr = [1,1,1,2,2,2,2,3,4,5,6,6,6,8,9]
    ob = Solution()
    print(ob.remove_duplicate(arr))
    print(arr)
    

