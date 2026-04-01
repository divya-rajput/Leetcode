class Solution:
    def trap(self, height: list[int]) -> int:
       #Intition : we need max and min at each position 
        i,j = 0,len(height)-1
        min_h, max_h, ans = 0,0,0
        while i < j:
            min_h = min(height[i], height[j])
            max_h = max(min_h, max_h)
            ans += (max_h - min_h)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
        