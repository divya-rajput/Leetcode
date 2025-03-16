#Complexity analysis 
#Time complexity- O(logn), Space complexity- O(1)
def binarySearch(array, target):
	left = 0
	right = len(array)-1
	
	while left <= right:
		mid = (left + right) // 2
		if(target > array[mid]):
			left = mid + 1
		elif(target < array[mid]):
			right = mid - 1
		else: 
			return mid			
	return -1

if __name__ == "__main__":
    array = [0,1,21,33,45,61,71,72,73]
    target = 33
    print("Output=",binarySearch(array,target))