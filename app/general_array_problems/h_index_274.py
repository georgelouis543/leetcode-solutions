from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        hash_map = {}

        # For example, take h = 3, [6, 5, 3, 3, 0]
        # Are there 'at least' 3 papers >= 3 citations?
        # 4 papers >= 3 citations (True)

        least_papers = 1
        h = 0
        for c in citations:
            if c >= least_papers:
                h = least_papers
            else:
                break
            least_papers += 1

        return h
