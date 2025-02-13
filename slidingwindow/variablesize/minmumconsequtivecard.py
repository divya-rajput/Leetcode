"""
Leetcode: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

"""
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        res = set()
        start, end = 0,0
        ans_len = float("inf")
        flag = 0
        while end < len(cards):
            while cards[end] in res:
                flag = 1
                ans_len = min(ans_len,len(res))
                res.remove(cards[start])
                start += 1
            res.add(cards[end])
            end += 1
        if flag == 0:
            return -1
        return ans_len+1
        
    
if __name__ == "__main__":
    ob = Solution()
    cards1 = [3,4,2,3,4,7]
    cards2 = [1,0,5,3]
    print(ob.minimumCardPickup(cards1))
    print(ob.minimumCardPickup(cards2))
