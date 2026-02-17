class Solution:
    def is_possible(self,bloomDay,day,m,k):
        count=0
        boquet=0
        for bloom in bloomDay:
            if bloom<=day:
                count+=1
                if count==k:
                    boquet+=1
                    count=0
            else:
                count=0
        return boquet>=m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        total_flower=m*k
        if total_flower>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if self.is_possible(bloomDay,mid,m,k):
                ans=mid  # you can also return low as consider opposite polarity case no need to save mid in answer. For bs in answer returning low gives correct value
                high=mid-1
            else:
                low=mid+1
        return ans