class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0: return 0
        nums.sort()
        longest=1;cnt=0
        lastSmaller=float('-inf')
        for i in range(n):
            if nums[i]-1==lastSmaller:
                cnt+=1
                lastSmaller=nums[i]
            elif nums[i]!=lastSmaller:
                cnt=1
                lastSmaller=nums[i]
            longest=max(longest,cnt)
        return longest 