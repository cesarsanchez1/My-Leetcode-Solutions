class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniqueArr1 = list(set(nums1))
        uniqueArr2 = list(set(nums2))
        
        set1 = set(nums1)
        set2 = set(nums2)
        a = []
        b = []
        for i in range(len(uniqueArr1)):
            if uniqueArr1[i] not in set2:
                a.append(uniqueArr1[i])
        for i in range(len(uniqueArr2)):
            if uniqueArr2[i] not in set1:
                b.append(uniqueArr2[i])
        return [a,b]
                
        
        