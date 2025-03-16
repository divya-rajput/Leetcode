#Complexity analysis 
#Time complexity- O(n), Space complexity- O(1)

def isPalindrome(string):    
	return string == string[::-1]
if __name__ == "__main__":
    string = "abcdcba"
    print("Output=",isPalindrome(string))