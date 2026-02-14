import math
class Solution:

    def calculateHrs(self,piles,hrs):
        total_hrs=0
        for bananas in piles:
            total_hrs+=math.ceil(bananas/hrs)
        return total_hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_el=max(piles)
        low,high,ans=1,max_el,-1
        while low<=high:
            mid=(low+high)//2
            req_hrs=self.calculateHrs(piles,mid)
            if req_hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
