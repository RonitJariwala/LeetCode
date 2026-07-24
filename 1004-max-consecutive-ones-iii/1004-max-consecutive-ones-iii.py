class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen,n=0,len(nums)
        l,r,zeros=0,0,0
        while r<n:
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen