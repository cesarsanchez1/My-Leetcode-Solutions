class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        dictionary.sort()
        
        mySet = set(dictionary)
        
        wordBank = sentence.split()
        
        bank = []
        
        for word in wordBank:
            temp = ""
            for letter in word:
                temp += letter
                if temp in mySet:
                    break
            if temp == "":
                bank.append(word)
            else:
                bank.append(temp)
    
        return ' '.join(bank)
        
        
        
        