class Solution:

    def bfirst(self,nums,target):
        left,right=0,len(nums)-1
        first=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                first=mid
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return first

    def blast(self,nums,target):
        last=-1
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                last=mid
                left=mid+1
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return last


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.bfirst(nums,target)
        last=self.blast(nums,target)
        return [first,last]
        #return (last-first+1) ## count of occurneces
