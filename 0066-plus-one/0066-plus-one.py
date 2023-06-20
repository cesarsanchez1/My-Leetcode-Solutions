class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""

        for item in digits:
            temp+=str(item)

        myInt = int(temp)+1

        res = []

        for item in str(myInt):
            res.append(int(item))
        
        return res