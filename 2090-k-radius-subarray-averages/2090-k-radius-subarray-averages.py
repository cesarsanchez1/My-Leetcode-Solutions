class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        arr = [-1]*k
        currSum = 0
        scope = (k*2)+1

        if len(nums)>=1 and k == 0:
            print("0")
            return nums

        if scope > len(nums):
            print("1")
            return [-1]*len(nums)

        if scope == len(nums):
            print("2")
            for i in range(scope):
                currSum += nums[i]
            average = int(currSum/scope)
            arr.append(average)
            arr.extend([-1]*k)
            return arr
        
        if scope < len(nums):
            print("3")
            for i in range(scope):
                currSum += nums[i]
            average = int(currSum/scope)
            arr.append(average)

            left = 0
            for right in range(scope, len(nums)):
                currSum -= nums[left]
                currSum += nums[right]
                average = int(currSum/scope)
                arr.append(average)
                left+=1
            arr.extend([-1]*k)
            return arr
        return [-1]
        



        