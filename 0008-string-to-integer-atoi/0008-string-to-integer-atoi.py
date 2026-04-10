class Solution:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1


    def helper(self,s,i,num,sign):
        if i>=len(s) or not s[i].isdigit():
            return num*sign
        num=num*10+int(s[i])
        if sign*num<=self.INT_MIN:
            return self.INT_MIN
        if sign*num>=self.INT_MAX:
            return self.INT_MAX
        return self.helper(s,i+1,num,sign)

    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        sign=1
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            sign=-1 if s[i]=='-' else 1
            i+=1
        return self.helper(s,i,0,sign)



    ''' Recursive extra stack O(N)
    def myAtoi(self, s: str) -> int:
        INT_MIN=-2**31
        INT_MAX=2**31-1
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        sign=1
        if i<n and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
                sign=-1
            i+=1
        num=0
        while i<n and s[i].isdigit():
            digit=int(s[i])
            num=num*10+digit
            if sign==1 and num>=INT_MAX:
                return INT_MAX
            if sign==-1 and num>=abs(INT_MIN):
                return INT_MIN
            i+=1
        return num*sign
        '''