#Complexity analysis 
#Time complexity- O(n), Space complexity- O(d), where d is the greatest depth of "special" arrays in an array
def productSum(array,multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element,multiplier +1)
        else:
            sum += element 
    return sum * multiplier


if __name__ == "__main__":
    array = [5,2,[7,-1],3,[6,[-13,8],4]]
    print("Output=",productSum(array))