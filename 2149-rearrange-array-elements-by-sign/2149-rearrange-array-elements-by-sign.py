class Solution:
    '''
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos,neg=[],[]
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])
            else: 
                neg.append(nums[i])
        for i in range(n//2):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        return nums
    '''
    # Little Better Solution
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos_index,neg_index=0,1
        for i in range(n):
            if nums[i]>0:
                ans[pos_index]=nums[i]
                pos_index+=2
            else:
                ans[neg_index]=nums[i]
                neg_index+=2
        return ans