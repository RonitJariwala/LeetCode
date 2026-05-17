class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # base
        if dividend==divisor: return 1
        if dividend==-2**31 and divisor==-1:
            return 2**31-1
        if divisor==1:
            return dividend
        isPos=True
        if dividend>=0 and divisor<0:
            isPos=False
        elif dividend<0 and divisor>0:
            isPos=False
        n=abs(dividend)
        d=abs(divisor)
        ans=0
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)):
                cnt+=1
            ans+=1<<cnt
            n=n-(d*(1<<cnt))
            
        if ans>2**31-1 and isPos:
            return 2**31-1
        if ans>2**31-1 and not isPos:
            return -2**31
        return ans if isPos else -1*ans