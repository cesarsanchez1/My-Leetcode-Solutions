class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on start points (and end points if start points are equal)
        intervals.sort(key=lambda x : (x[0],-x[1]))
        counter = 0
        uncovered_end = float('-inf')

        for interval in intervals:
            start, end = interval

            if end > uncovered_end:
                uncovered_end = end
                counter+=1

        return counter

            