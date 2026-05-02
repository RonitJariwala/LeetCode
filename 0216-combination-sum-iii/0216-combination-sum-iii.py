class Solution:
    def findSub(self,ind,k,target,ds,ans):
        if len(ds)==k:
            if target==0:
                ans.append(list(ds))
            return
        for i in range(ind,10):
            if i>target:
                break
            ds.append(i)
            self.findSub(i+1,k,target-i,ds,ans)
            ds.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ds=[]
        ans=[]
        self.findSub(1,k,n,ds,ans)
        return ans