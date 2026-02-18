class Solution:
    
    def calculateDays(self,weights,cap):
        days=1;load=0
        for w in weights:
            if load+w>cap:
                days+=1
                load=w
            else:
                load+=w
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights) # important to find the max capacity !observation
        while low<=high:
            mid=(low+high)//2
            reqDays=self.calculateDays(weights,mid)
            if reqDays<=days:
                high=mid-1
            else:
                low=mid+1
        return low