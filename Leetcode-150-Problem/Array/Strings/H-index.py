class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Time- O(n log n), Space- O(1)
        # Leetcode-274: hhttps://leetcode.com/problems/h-index/description/
        """
        Intuition: We sort the citations in descending order so the most‑cited papers come first. 
        Then we scan the list and find the first position where the paper’s citation count is less than the number of papers considered so far. 
        That position is the h‑index. If this never happens, the h‑index is simply the total number of papers.
        """
        
        # Copy the below code logic to Leetcode code editor
        citations.sort(reverse=True)

        for index, citation in enumerate(citations):
            if index >= citation:
                return index
        return len(citations)