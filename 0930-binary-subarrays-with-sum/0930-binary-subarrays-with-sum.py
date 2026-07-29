class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums,goal)-self.atMost(nums,goal-1)


    def atMost(self, nums: List[int], goal: int) -> int:
        if goal<0: return 0
        cnt,n=0,len(nums)
        left,right,sum=0,0,0
        while right<n:
            sum+=nums[right]
            while sum>goal:
                sum-=nums[left]
                left+=1
            cnt=cnt+(right-left+1)
            right+=1
        return cnt