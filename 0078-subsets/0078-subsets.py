class Solution:
    def recur(self,ind,sum,arr,res):
        if len(arr)==ind:
            res.append(sum)
            return
        self.recur(ind+1,sum+[arr[ind]],arr,res)
        self.recur(ind+1,sum,arr,res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.recur(0,[],nums,res)
        res.sort()
        return res