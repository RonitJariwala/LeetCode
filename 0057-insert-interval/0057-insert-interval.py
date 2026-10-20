class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]
        i=0
        n=len(intervals)

        # Add all the intervals completely before the new interval
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1

        # Merge all overlapping intervals into one massive interval
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        
        #add fully merged interval
        res.append(newInterval)

        #Add all remaining intervals
        while i<n:
            res.append(intervals[i])
            i+=1
        
        return res