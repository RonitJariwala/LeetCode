class Solution:
    def calculatePartitions(self,nums,max_sum):
        partitions=1;total_sum=0
        for num in nums:
            if num+total_sum<=max_sum:
                total_sum+=num
            else:
                partitions+=1
                total_sum=num
        return partitions

    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            part=self.calculatePartitions(nums,mid)
            if part<=k:
                high=mid-1
            else:
                low=mid+1
        return low