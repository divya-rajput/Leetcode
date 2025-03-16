#Complexity analysis 
#Time complexity- O(nlogn), Space complexity- O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	if(fastest):
		return maximumSumSpeeds(redShirtSpeeds, blueShirtSpeeds)
	else:
		return minimumSumSpeeds(redShirtSpeeds, blueShirtSpeeds)
	
def maximumSumSpeeds(redShirtSpeeds, blueShirtSpeeds):
    maxSum = 0
    i = 0 
    j = len(blueShirtSpeeds)-1
    while i < len(redShirtSpeeds):
        maxSum += max(redShirtSpeeds[i],blueShirtSpeeds[j])
        i += 1
        j -= 1
    return maxSum
	
def minimumSumSpeeds(redShirtSpeeds, blueShirtSpeeds):
    maxSum = 0
    i = 0
    j = 0
    while i < len(redShirtSpeeds):
        maxSum += max(redShirtSpeeds[i],blueShirtSpeeds[j])
        i += 1
        j += 1
    return maxSum
    
#Main method to run the test.
if __name__ == "__main__":
    redShirtSpeeds = [5,5,3,9,2]
    blueShirtSpeeds = [3,6,7,2,1]
    fastest = True
    print("Output=",tandemBicycle(redShirtSpeeds, blueShirtSpeeds,fastest))