class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_val=max(nums)
        hash_cn=[0]*(max_val+1)
        while len(nums)>0:
            x=nums.pop(0)
            hash_cn[x]+=1
        for i in range(len(hash_cn)):
            while hash_cn[i]>0:
                nums.append(i)
                hash_cn[i]-=1
        return nums












