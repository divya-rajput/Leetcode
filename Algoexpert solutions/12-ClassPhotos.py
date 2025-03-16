#Complexity analysis 
#Time complexity- O(nlogn), Space complexity- O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	flag = 0
	if(redShirtHeights[0] < blueShirtHeights[0]):
		for i in range(len(redShirtHeights)):
			if(redShirtHeights[i] < blueShirtHeights[i]):
				continue
			else:
				flag = 1
	else:
		for j in range(len(redShirtHeights)):
			if(redShirtHeights[j] > blueShirtHeights[j]):
				continue
			else:
				flag = 1
		
	if(flag == 0):
		return True
	else:
		return False
			
#Main method to run the test.
if __name__ == "__main__":
    redShirtHeights = [5,8,1,3,4]
    blueShirtHeights = [6,9,2,4,5]
    print("Output=",classPhotos(redShirtHeights, blueShirtHeights))