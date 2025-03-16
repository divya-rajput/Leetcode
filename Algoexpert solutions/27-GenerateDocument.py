#Complexity Analysis
#Time complexity: O(m+n), whee n is the number of characters and m is the length of the document. 
#Space complexity: O(c), where c is the number of unique characters in characters string.
def generateDocument(characters, document):
    # Write your code here.
    if (len(document) > len(characters)):
        return False
    else:
        #Logic: count the number of characters in character string and create ahash table and decrease the key value as the character found in document
        dic = {}
        for i in range(len(characters)):
            if characters[i] not in dic:
                dic[characters[i]] = 1
            else:
                dic[characters[i]] += 1
        for j in range(len(document)):
            if document[j] in dic and dic[document[j]] !=0:
                dic[document[j]] -= 1
            else:
                return False
        return True
                
if __name__ == "__main__":
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    print("Output=",generateDocument(characters,document))             