class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        check = list(set(arr))
        check.sort()

        rank = {}
        count = 1

        for item in check:
            rank[item] = count
            count +=1
        
        res = []

        for item in arr:
            res.append(rank[item])
        return res







       