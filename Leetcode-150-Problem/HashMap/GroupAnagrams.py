from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Time- O(n), Space- O(1)(Note: It can be considered as constant space as the alphabet only have 26 characters which is a conatnt number.)
        # Leetcode-49: https://leetcode.com/problems/group-anagrams/
        # Copy the below code logic
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
