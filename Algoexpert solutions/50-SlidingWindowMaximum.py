from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        i = k
        while i < len(nums):
            if i- q[0] >= k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
            i += 1
        return ans       
            
if __name__ == "__main__":
    obj = Solution()
    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3
    nums = [1,3,1]
    k = 2
    print(obj.maxSlidingWindow(nums,k))