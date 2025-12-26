class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x%10==0 and x!=0: return False
        rev=0; copy=x
        while x!=0:
            ld=x%10
            rev=rev*10+ld
            x=x//10
        return copy==rev
