class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time- O(n), Space- O(1)
        # Leetcode-88: https://leetcode.com/problems/merge-sorted-array/
        # Copy the below code logic
        while n > 0:
            if nums1[m-1] >= nums2[n-1] and m > 0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

