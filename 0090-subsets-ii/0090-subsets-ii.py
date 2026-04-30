class Solution:
    def backtrack(self,start,nums,current,res):
        res.append(list(current))
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            current.append(nums[i])
            self.backtrack(i+1,nums,current,res)
            current.pop()

    def subsetsWithDup(self,nums):
        nums.sort()
        res=[]
        self.backtrack(0,nums,[],res)
        return res
