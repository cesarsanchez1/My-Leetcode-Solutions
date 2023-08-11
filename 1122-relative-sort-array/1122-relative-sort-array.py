class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        set2 = set(arr2)
        
        end = []

        for item in arr1:
            if item not in set2:
                end.append(item)
        
        end.sort()

        uniqueSet = set()
        unique = []

        for item in arr2:
            if item not in uniqueSet:
                unique.append(item)
            uniqueSet.add(item)

        freq = {}
            
        for item in arr1:
            freq[item] = freq.get(item, 0) + 1

        res = []
        
        for item in unique:
            temp = [item]*freq[item]
            res.extend(temp)
        res.extend(end)
        return res




        


            
