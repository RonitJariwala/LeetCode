class Solution:

    def findCombination(self,ind,arr,target,ds,ans): 
        if ind==len(arr):
            if target==0:
                ans.append(list(ds))
            return
        # left recursion
        if arr[ind]<=target:
            ds.append(arr[ind])
            self.findCombination(ind,arr,target-arr[ind],ds,ans)
            ds.pop() # backtrack
        self.findCombination(ind+1,arr,target,ds,ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        ans=[]
        self.findCombination(0,candidates,target,ds,ans)
        return ans