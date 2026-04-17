class Solution:
    def generateAll(self,curr,open,close,n,res):
        if len(curr)==2*n:
            res.append(curr)
            return
        if open<n:
            self.generateAll(curr+'(',open+1,close,n,res)
        if close<open:
            self.generateAll(curr+')',open,close+1,n,res)

    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.generateAll("",0,0,n,res)
        return res