class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        # single element return
        if n==1:
            return nums[0] 
        # return first element if unqiue
        if nums[0]!=nums[1]:
            return nums[0]
        # return last element if unqiue
        if nums[-1]!=nums[-2]:
            return nums[-1]
        low,high=1,n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            # If mid is in the left half (pairing is valid)
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return -1



