#Complexity analysis 
#Time complexity- O(n^2), Space complexity- O(1)
def bubbleSort(a):
	n = len(a)
	for i in range(n):
		swapped = False
		for j in range(0,n-i-1):
			if(a[j] > a[j+1]):
				a[j], a[j+1] = a[j+1], a[j]
				swapped = True
		if swapped == False:
			break
	return a

if __name__ == "__main__":
    array = [0,74,21,87,45,61,71,72,73]
    print("Output=",bubbleSort(array))