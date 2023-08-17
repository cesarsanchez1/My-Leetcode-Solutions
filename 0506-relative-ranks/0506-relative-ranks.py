class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        check = score[:]
        check.sort()
        check = check[::-1]

        freq = {}
        pos = 1

        for item in check:
            freq[item] = pos
            pos += 1

        res = []

        for item in score:
            ranking = freq[item]
            if ranking == 1:
                res.append(rank[0])
            elif ranking == 2:
                res.append(rank[1])
            elif ranking == 3:
                res.append(rank[2])
            else:
                res.append(str(freq[item]))

        return res


