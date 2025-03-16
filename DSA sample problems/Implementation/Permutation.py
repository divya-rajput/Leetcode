

s1 = "aaaaa"
s2 = "aaaab"
d1 = {}
d2 = {}


#Building dictionaries
for i in s1:
        if i not in d1:
            d1[i] = 0
        else:
            d1[i] = d1[i] + 1

for j in s2:
        if j not in d2:
            d2[j] = 0
        else:
            d2[j] = d2[j] + 1
# print("Dictionary 1: ", d1)
# print("Dictionary 2: ", d2)
flag = 0
#printing values in dictionaries
for i in d1:
    for j in d2:
        if(i == j ):
            if(d1[i] == d2[j] or d2[j] > d1[i]):
                continue
            else:
                flag = 1
                break
if(flag == 0):
    print("S1 is present in S2")
else:
    print("S1 is not present in S2")





