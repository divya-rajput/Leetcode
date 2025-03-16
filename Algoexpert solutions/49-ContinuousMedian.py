from heapq import heappush as push, heappop as pop

 
def solve(nums: list) -> list:
    min_list = list()
    max_list = list()
    
    def balance():
        if abs(len(min_list) - len(max_list)) <= 1:
            return
        if len(min_list) > len(max_list):
            value = pop(min_list)
            push(max_list, -value)
        else:
            value = pop(max_list)
            push(min_list, -value)
    
    def get_median():
        if len(min_list) < len(max_list):
            val = pop(max_list)
            push(max_list, val)
            return -val
        elif len(min_list) > len(max_list):
            val: list = pop(min_list)
            push(min_list, val)
            return val
        else:
            val1 = pop(max_list)
            push(max_list, val1)
            val2 = pop(min_list)
            push(min_list, val2)
            return (val2 - val1) / 2
    
    def insert(value):
        if len(max_list) == 0 and len(min_list) == 0:
            push(min_list, value)
            return
        median = get_median()
        if value > median:
            push(min_list, value)
        else:
            push(max_list, -value)
        balance()
    
    ans = []
    for num in nums:
        if num[0] == 1:
            insert(num[1])
        else:
            ans.append(get_median())
    return ans
            
input = [
	[1, 3],
	[2],
	[1, 4],
	[1, 7],
	[2],
	[1, 5],
	[2],
	[1, 4],
	[2],
	[1, 10],
	[2]
]
print(solve(input))
 
expected_output = [3, 4, 4.5, 4, 4.5]

assert expected_output == solve(input)








