class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen=0
        cnt=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                cnt+=1
            else: cnt=0
            maxLen=max(cnt,maxLen)
        return maxLen