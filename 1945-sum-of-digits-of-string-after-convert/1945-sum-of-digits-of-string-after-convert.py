class Solution:
    def getLucky(self, s: str, k: int) -> int:
    
        temp = ""
        
        for letter in s:
            letter_ord = ord(letter)-ord('a')+1
            temp += str(letter_ord)

        for i in range(k):
            run_sum = 0
            for letter in temp:
                run_sum += int(letter)
            temp = str(run_sum)
        return int(temp)
            



        return 0