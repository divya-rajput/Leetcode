#Complexity analysis 
#Time Complexity: O(n*m) and Space complexity: O(n*m), where n is the number of words and m is the length of the longest string
def semordnilap(words):
    wordsSet = set(words)
    semordnilapPairs = []
    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word:
            semordnilapPairs.append([word,reverse])
            wordsSet.remove(word)
            wordsSet.remove(reverse)
    return semordnilapPairs

if __name__ == "__main__":
    words = ["desserts", "stressed", "hello"]
    print("Output=",semordnilap(words))