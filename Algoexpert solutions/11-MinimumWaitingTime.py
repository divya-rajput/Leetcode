#Complexity analysis 
#Time complexity- O(nlogn), Space complexity- O(1)
def minimumWaitingTime(queries):
	queries = sorted(queries)
	i,n = 0,len(queries)
	value,newval = 0,0
	while i < n:
		if i == 0:
			value = 0
		else:
			value += queries[i-1]
		newval += value
		i += 1
	return newval

#Main method to run the test.
if __name__ == "__main__":
    queries = [3,2,1,2,6]
    print("Output=",minimumWaitingTime(queries))