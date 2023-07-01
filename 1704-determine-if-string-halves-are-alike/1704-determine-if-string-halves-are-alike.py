class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelSet = set("aeiouAEIOU")

        a = s[0:int(len(s)/2)]
        b = s[int(len(s)/2):len(s)]

        counter1 = 0
        counter2 = 0

        for letter in a:
            if letter in vowelSet:
                counter1+=1

        for letter in b:
            if letter in vowelSet:
                counter2+=1
            
        if counter1 == counter2:
            return True
        return False
