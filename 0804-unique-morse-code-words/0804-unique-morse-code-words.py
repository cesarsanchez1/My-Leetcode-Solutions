class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        alpha = "abcdefghijklmnopqrstuvwxyz"

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
        "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
        ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        freq = {}
        
        for i in range(26):
            freq[alpha[i]] = morse[i]

        unique = set()
        
        for word in words:
            temp = ""
            for letter in word:
                temp += freq[letter]
            unique.add(temp)
        return len(unique)
            


        