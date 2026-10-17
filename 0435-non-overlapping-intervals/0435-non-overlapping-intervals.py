class Solution:

    def buildInterval(self,intervals):
        return [intervals[0],intervals[1]]

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda interval:interval[1])
        remove_cnt=0
        last_end_time=intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0]<last_end_time:
                remove_cnt+=1
            else:
                last_end_time=intervals[i][1]
        return remove_cnt