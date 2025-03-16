#Complexity analysis 
#Time complexity- O(n), Space complexity- O(1)
def caesarCipherEncryptor(string, key):
    # Write your code here.
	s = ""
	if(key > 26):
		key = key % 26
	for i in range(len(string)):
		if(ord(string[i])+key >=97 and ord(string[i])+key <= 122):
			s += chr(ord(string[i])+key)
			
		else:
			s += chr(ord(string[i])+key-26)	
	return s

if __name__ == "__main__":
    string = "xyz"
    key = 2
    print("Output=",caesarCipherEncryptor(string,key))