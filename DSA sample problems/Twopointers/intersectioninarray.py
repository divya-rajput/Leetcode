"""
Finding Intersection of Two Sorted Arrays
Intuition: Since the arrays are sorted, we know that the smaller elements will always come first. Also, repetition is allowed.
Time complexity: O(m+n)
Space complexity: O(min(m,n))
"""

class solution():
    def __init__(self):
        pass
    def merge_sorted(self,a: list[int],b: list[int]) -> list:
        i,j = 0,0
        res = []
        while i < len(a) and j <len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res

if __name__ == "__main__":
    ob = solution()
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [1,2,3,3,3,4,7,8,9]
    print(ob.merge_sorted(arr1,arr2))