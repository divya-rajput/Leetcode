class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if count > 1:
                    return False
                
                # Check if modifying nums[i-1] or nums[i] works
                if i - 2 >= 0 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        
        return True
if __name__ == "__main__":
    obj = Solution()
    nums = [-1,4,2,3]
    print(obj.checkPossibility(nums))
