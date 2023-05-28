class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # CASE WHERE SIZE == 1 AND flowerbed = [0] and n==1 Returns True
        if len(flowerbed)==1 and flowerbed[0] == 0 and n<=1:
            return True
        # CASE WHERE SIZE == 1 AND flowerbed = [0] and n>1  RETURNS False
        if len(flowerbed)==1 and flowerbed[0] == 0 and n>1:
            return False
        # CASE WHERE SIZE == 1 AND flowerbed = [1] and n>=1 Returns False
        if len(flowerbed)==1 and flowerbed[0] == 1 and n>=1:
            return False

        counter = 0

        for i in range(len(flowerbed)):
            #LEFT EXTREME
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                counter+=1
            #INTERMEDIATE
            if (i!=0 and i!=len(flowerbed)-1) and (flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                counter+=1
            #RIGHT EXTREME
            if i==len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                counter+=1

        if counter >= n:
            return True
        else:
            return False