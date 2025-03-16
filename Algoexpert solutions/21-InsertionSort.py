#Complexity analysis 
#Time complexity- O(n^2), Space complexity- O(1)
def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        j = i 
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    array = [0,74,21,87,45,61,71,72,73]
    print("Output=",insertionSort(array))