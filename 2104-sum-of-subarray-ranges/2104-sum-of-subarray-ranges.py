class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for i in range(n):
            smallest,largest=nums[i],nums[i]
            for j in range(i+1,n):
                largest=max(nums[j],largest)
                smallest=min(nums[j],smallest)
                total+=(largest-smallest)
        return total
