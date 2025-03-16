#Complexity analysis 
#Time complexity- O(n), Space complexity- O(1)

def firstNonRepeatingCharacter(string):
    dict = {}
    count = 0
    for i in range(len(string)):
        if string[i] not in dict:
            count = 1
            dict[string[i]] = count   
        else:
            count += 1
            dict[string[i]] = count
    for i in range(len(string)):
        if dict[string[i]] == 1:
            return i
    return -1

if __name__ == "__main__":
    string = "abcabcabcddfabcd"
    print("Output=",firstNonRepeatingCharacter(string))