class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #Solution- 1
        output = []
        for num in nums1:
            found = False
            next_greater = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    found = True
                elif found and nums2[i] > num:
                    next_greater = nums2[i]
                    break
            output.append(next_greater)

        return output

        #solution: 2- Monotonic stack

        stack = []
        next_greater = {}

        # Build next greater map for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1

        # Build output for nums1
        return [next_greater[num] for num in nums1]