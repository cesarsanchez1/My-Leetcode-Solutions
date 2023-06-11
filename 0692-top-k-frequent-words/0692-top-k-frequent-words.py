class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = [[]]*500
        freq = {}
        maxFreq = 0

        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
            maxFreq = max(maxFreq, freq[word])
        
        uniqueWords = list(set(words))

        for word in uniqueWords:
            if arr[freq[word]] == []:
                arr[freq[word]] = [word]
            else:
                arr[freq[word]].append(word)
        
        res = []

        if maxFreq == 0:
            return []

        for i in range(maxFreq, -1, -1):
            if arr[i] != []:
                arr[i].sort()
                res.extend(arr[i])

        if k >= len(res):
            return res
        return res[0:k]





