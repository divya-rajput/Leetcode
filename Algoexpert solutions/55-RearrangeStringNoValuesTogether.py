# Input
# s= "aababaa"
# output = "ababa"
from heapq import heappush,heappop
#Create a dic with storing the frequency of character
def rearrange(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    # creating a heap
    h = []
    for val in d:
        heappush(h, (-d[val],val))

    print(h)
    result = ""
    while len(h) > 1:
        f1,c1 = heappop(h)
        f2,c2 = heappop(h)
        result += c1
        result += c2
        print(f1,f2)
        if abs(f1) > 1:
            heappush(h,(f1+1,c1))
        if abs(f2) > 1:
            heappush(h,(f2+1,c2))
    if h:
        fr,ch = h[0]
        if abs(fr) > 1:
            return ""
        else:
            result += ch
    return result

s= "aabab"
print(rearrange(s))

def rearrange2(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    # creating a heap
    h = []
    for val in d:
        heappush(h, (-d[val],val))
    result = ""
    while h:
        f,c = heappop(h)
        if result == "":
            result += c
            f += 1
            if f:
                heappush(h, (f,c))
            continue
        if result[-1] == c:
            if h:
                f1, c1 = heappop(h)
                result += c1
                f1 += 1
                heappush(h, (f,c))
                if f1 != 0:
                    heappush(h, (f1,c1))
                continue
            else:
                return ""
        result += c
        f += 1
        if f:
            heappush(h, (f,c))
    return result

s= "aabab"
print(rearrange2(s))