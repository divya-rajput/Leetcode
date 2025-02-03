class Solution(object):
    def __init__(self):
        pass
    def reverse(self, st: str, l: int, r: int)-> bool:
        if l > r:
            return
        arr[l],arr[r] = arr[r], arr[l]
        return self.reverse(st,l+1,r-1)
    
if __name__ == "__main__":
    ob = Solution()
    arr = [45,56,68,78,100]
    ob.reverse(arr, 0, len(arr)-1)
    print(arr)








