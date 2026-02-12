class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        low,high=1,n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                low=mid+1 #eliminate left
            elif nums[mid]>nums[mid+1]:
                high=mid-1 #eliminate right
            else:  # [1,2,1,3,2] for this test suppose mid is at bottom then
                low=mid+1
        return -1