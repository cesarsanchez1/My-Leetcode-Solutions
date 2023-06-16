class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        uniqueTuple = set()
        
        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')]+=1
            uniqueTuple.add(tuple(count))
            if tuple(count) in freq:
                freq[tuple(count)].append(word)
            else:
                freq[tuple(count)] = [word]
        
        res = []

        for item in list(uniqueTuple):
            res.append(freq[item])

        return res








            
