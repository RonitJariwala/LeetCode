class Solution:
    ''' Brute O(NlogN)+O(2N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        i=0
        ans=[]
        while i<n:
            start=intervals[i][0]
            end=intervals[i][1]
            j=i+1
            while j<n and intervals[j][0]<=end:
                end=max(end,intervals[j][1])
                j+=1
            ans.append([start,end])
            i=j
        return ans
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for int in intervals:
            if not ans or ans[-1][1]<int[0]:
                ans.append(int)
            else:
                ans[-1][1]=max(ans[-1][1],int[1])
        return ans