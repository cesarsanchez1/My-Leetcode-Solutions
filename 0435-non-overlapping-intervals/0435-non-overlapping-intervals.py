class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])    # sort intervals based on their end times

        counter = 0     # declare a counter for the minimum number of intervals that need to be removed

        prev = float('-inf')

        for interval in intervals:
            if interval[0] < prev:
                counter+=1
            else:
                prev = interval[1]
            
        return counter

