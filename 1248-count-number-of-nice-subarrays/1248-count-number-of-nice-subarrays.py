class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k)-self.atMost(nums,k-1)

    def atMost(self,nums,k):
        if k<0: return 0
        cnt,n=0,len(nums)
        left,right,sum=0,0,0
        while right<n:
            sum+=(nums[right]%2)
            while sum>k:
                sum-=(nums[left]%2)
                left+=1
            cnt+=(right-left+1)
            right+=1    
        return cnt
