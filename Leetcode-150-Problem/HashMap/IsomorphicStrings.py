class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time- O(n), Space- O(n)
        # Leetcode-205: https://leetcode.com/problems/isomorphic-strings/
        # Copy the below code logic
        
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        print(map1,map2)
        if map1 == map2:
            return True
        return False

        # Solution-2 Using Hashmap
        # Time- O(n), Space- O(1)
        # Leetcode-205: https://leetcode.com/problems/isomorphic-strings/
        # Copy the below code logic

        mapST, mapTS = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True