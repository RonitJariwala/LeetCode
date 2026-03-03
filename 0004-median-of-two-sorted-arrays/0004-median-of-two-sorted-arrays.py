import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Ensure nums1 is the smaller array to optimize binary search
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        n1,n2=len(nums1),len(nums2)
        n=n1+n2
        low,high=0,n1
        while low<=high:
            # 2. Partition nums1 and nums2
            mid1=(low+high)//2
            mid2=(n+1)//2-mid1
            # 3. Handle edge cases with -infinity and +infinity
            # If partition is at 0, there is no Left element (use -inf)
            # If partition is at length, there is no Right element (use +inf)
            l1=float('-inf') if mid1==0 else nums1[mid1-1]
            r1=float('inf') if mid1==n1 else nums1[mid1]
            l2=float('-inf') if mid2==0 else nums2[mid2-1]
            r2=float('inf') if mid2==n2 else nums2[mid2]
            # 4. Check if the partition is valid
            if l1<=r2 and l2<=r1:
                # correct partition found !!
                # for odd
                if n%2==1:
                    return float(max(l1,l2))
                # for even
                else: 
                    return float(max(l1,l2)+min(r1,r2))/2.0
            elif l1>r2: # eliminate right
                high=mid1-1
            else:       # eliminate left
                low=mid1+1
        return 0.0



























