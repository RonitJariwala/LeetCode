class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k)-self.atMost(nums,k-1)

    def atMost(self,nums,k):
        freq={}
        left,right,count=0,0,0
        while right<len(nums):
            if nums[right] not in freq or freq[nums[right]]==0:
                k-=1
            freq[nums[right]]=freq.get(nums[right],0)+1
            while k<0:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    k+=1
                left+=1
            count+=(right-left+1)
            right+=1
        return count