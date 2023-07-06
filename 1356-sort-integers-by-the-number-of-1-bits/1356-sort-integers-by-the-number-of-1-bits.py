class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def countOnes(check: str):
            counter = 0
            for item in check:
                if item == "1":
                    counter += 1
            return counter

        freq = {}
        countSet = set()

        for item in arr:
            biNum = bin(item)
            count = countOnes(str(biNum[2:]))
            countSet.add(count)

            if count in freq:
                freq[count].append(item)
            else:
                freq[count] = [item]
        
        countSetList = list(countSet)
        countSetList.sort()

        res = []

        for item in countSet:
            tempArr = freq[item]
            tempArr.sort()
            res.extend(tempArr)

        return res



            