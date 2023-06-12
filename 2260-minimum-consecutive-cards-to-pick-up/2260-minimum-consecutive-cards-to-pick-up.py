class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        left = 0
        res = float('Inf')
        freq = {}
        
        for right in range(n):
            freq[cards[right]] = freq.get(cards[right], 0) + 1

            while freq[cards[right]] > 1 and left < right:
                res = min(res, right-left+1)
                freq[cards[left]]-=1
                left+=1
        
        if res == float('Inf'):
            return -1

        return res
