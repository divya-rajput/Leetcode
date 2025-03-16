#Complexity analysis 
#Time complexity- O(n), Space complexity- O(n)
def runLengthEncoding(string):
    # Write your code here.
    encodedList =[]
    currentLen = 1
    last = len(string) - 1
    for i in range(1, len(string)):
        currChar = string[i]
        prevChar = string[i-1]  #It will not throw any error since we are starting from 1
        if currChar != prevChar or currentLen == 9:
            encodedList.append(str(currentLen))
            encodedList.append(prevChar)
            currentLen = 0
        currentLen += 1
    #edge cases
    encodedList.append(str(currentLen))
    encodedList.append(string[last])
    return "".join(encodedList)

if __name__ == "__main__":
    string = "AAAAAAAAAAAAABBCCCCDD"
    print("Output=",runLengthEncoding(string))
