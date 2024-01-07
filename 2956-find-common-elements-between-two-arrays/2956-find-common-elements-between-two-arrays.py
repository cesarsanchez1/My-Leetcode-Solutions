class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        counter1 = 0
        counter2 = 0

        for i in range(len(nums1)):
            if nums1[i] in set2:
                counter1+=1
        
        for j in range(len(nums2)):
            if nums2[j] in set1:
                counter2+=1
        
        return [counter1, counter2]



