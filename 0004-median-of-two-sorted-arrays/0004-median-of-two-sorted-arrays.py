class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1[:]
        nums3.extend(nums2)

        nums3.sort()

        print(nums3)
        
        if len(nums3)%2!=0:
            index = int(len(nums3)/2)
            return nums3[index]
        else:
            index1 = int(len(nums3)/2) - 1
            index2 = int(len(nums3)/2)
            return (nums3[index1]+nums3[index2])/2
