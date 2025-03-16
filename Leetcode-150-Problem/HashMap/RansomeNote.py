class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time- O(n), Space- O(1)(Note: It can be considered as constant space as the alphabet only have 26 characters which is a conatnt number.)
        # Leetcode-383: https://leetcode.com/problems/ransom-note/
        # Copy the below code logic
        dict = {}
        for ch in magazine:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] += 1
        print(dict)
        for ch in ransomNote:
            if ch in dict:
                if dict[ch] <= 0:
                    return False
                dict[ch] -= 1
            else:
                return False
        print(dict)
        return True