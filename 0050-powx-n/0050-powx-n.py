class Solution:
    def power(self,x,n):
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            return self.power(x*x,n//2)
        return x*self.power(x,n-1)
        

    def myPow(self, x: float, n: int) -> float:
        return self.power(x,n)