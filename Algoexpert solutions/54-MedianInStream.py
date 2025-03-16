from  heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.left = []    #Max Heap (-)
        self.right = []      #Min Heap 
        
    def addNum(self, num: int) -> None:            
        if len(self.left) == 0 or num <= -self.left[0]:
            heappush(self.left, -num)
        else:
            heappush(self.right, num)
        self.rebalance()
    
    def rebalance(self):
        ll = len(self.left)
        lr = len(self.right)
        if ll > lr and ll - lr > 1:
            heappush(self.right, -heappop(self.left)) 
        elif lr > ll and lr - ll > 1:
            heappush(self.left, -heappop(self.right))
        print("left:", self.left)
        print("right:", self.right)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            val = (-self.left[0] +self.right[0]) / 2
            return val
        else:
            if len(self.right) > len(self.left):
                return self.right[0]
            else:
                return -self.left[0] 
        
arr = []
m = MedianFinder()
m.addNum(3)
m.addNum(1)
m.addNum(6)
m.addNum(2)
m.addNum(4)
m.addNum(5)
print(m.findMedian())