class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        mySet = set()
        uniqueList = list(set(arr))
        for item in arr:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        for item in uniqueList:
            if freq[item] in mySet:
                return False
            mySet.add(freq[item])
        return True
                
            