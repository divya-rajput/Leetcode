#Complexity analysis 
#Time complexity- O(nlogn), Space complexity- O(1)
def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 1
    for coin in coins:
        if coin > currentChange:
            return currentChange
        currentChange += coin
    return currentChange

#Main method to run the test.
if __name__ == "__main__":
    coins = [5,7,1,1,2,3,22]
    print("Output=",nonConstructibleChange(coins))

