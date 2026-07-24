class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        maxCon=0
        cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            maxCon=max(maxCon,cnt)
        return maxCon