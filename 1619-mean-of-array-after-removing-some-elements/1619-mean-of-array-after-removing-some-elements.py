class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        range = int(len(arr)*0.05)
        mean = sum(arr[range:len(arr)-range])/len(arr[range:len(arr)-range])
        return mean