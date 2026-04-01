class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
             return ""
        minLen = min(len(x) for x in strs)
        l, h = 1, minLen
        while l <= h:
            mid = (l+h) // 2
            if self.isCommonPrefix(strs,mid):
                l = mid+1
            else:
                h = mid-1
        return strs[0][:(l+h)//2]
    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True