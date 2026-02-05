class Solution:
    def bsearch(self,nums,left,right,target):
        if left>right:
            return -1
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.bsearch(nums,mid+1,right,target)     
        else:
            return self.bsearch(nums,left,mid-1,target)


    def search(self, nums: List[int], target: int) -> int:
       return self.bsearch(nums,0,len(nums)-1,target)