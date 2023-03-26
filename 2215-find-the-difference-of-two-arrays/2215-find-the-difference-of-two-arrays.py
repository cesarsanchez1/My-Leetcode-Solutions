class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique1 = set(nums1)
        unique2 = set(nums2)

        a = list(unique1)
        b = list(unique2)

        res1 = []
        res2 = []

        for item in a:
            if item not in unique2:
                res1.append(item)

        for item in b:
            if item not in unique1:
                res2.append(item)
        
        return [res1,res2]
            


        