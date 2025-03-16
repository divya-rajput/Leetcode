#Complexity analysis 
#Time complexity- O(n^2), Space complexity- O(1)
def selectionSort(array):
    currIndex = 0
    while currIndex < len(array)-1:
        smallIndex = currIndex
        for i in range(currIndex +1, len(array)):
            if array[smallIndex] > array[i]:
                smallIndex = i
        swap(currIndex,smallIndex,array)
        currIndex +=1
    return array

def swap(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]

if __name__ == "__main__":
    array = [0,74,21,87,45,61,71,72,73]
    print("Output=",selectionSort(array))