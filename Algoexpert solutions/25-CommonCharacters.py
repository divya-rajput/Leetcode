#Complexity analysis 
#Time complexity- O(m * n), Space complexity- O(m), where n is the number of strings and m is the length of the longest string.

def commonCharacters(strings):
    # Write your code here.
    common_char = set(strings[0])
    for word in strings:
        temp = set()
        for letter in word:
            if letter in common_char:
                temp.add(letter)
        common_char = temp
    return list(common_char)

if __name__ == "__main__":
    string = ["abc","bcd","abaccd"]
    print("Output=",commonCharacters(string))