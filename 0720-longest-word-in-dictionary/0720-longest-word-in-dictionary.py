class Solution:
    def longestWord(self, words: List[str]) -> str:
        shortest = float('Inf')

        for word in words:
            shortest = min(shortest, len(word)) 

        if shortest > 1:
            return ""

        words.sort()
        words = words[::-1]
        uniqueSet = set(words)

        temp= ""
        wordReturn = ""

        count = 0
        arr = []

        currHighest  = 0
        
        for i in range(len(words)):
            temp = words[i]
            for j in range(len(words[i])):
                check = temp[0:len(temp)-j]
                print(check)
                if check in uniqueSet:
                    count+=1
                else:            
                    count = 0
                    break
                if count == len(temp):
                    count = 0
                    arr.append(temp)

        longest = 0
        for item in arr:
            longest = max(longest, len(item))

        res = []

        for item in arr:
            if len(item) == longest:
                res.append(item)

        return min(res)


                





        