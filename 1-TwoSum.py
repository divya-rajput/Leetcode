'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for i,n in enumerate(nums):
            if n not in record:
                record[target-n] = i
            else:
                return [record[n],i]
            
if __name__ == "__main__":
    obj = Solution()
    nums1 = [2,7,11,15]
    target1 = 9
    nums2 =[3,2,4]
    target2 = 6
    nums3 = [3,3]
    target3 = 6
    print("Output-1: ", obj.twoSum(nums1,target1))
    print("Output-2: ", obj.twoSum(nums2,target2))
    print("Output-3: ", obj.twoSum(nums3,target3))