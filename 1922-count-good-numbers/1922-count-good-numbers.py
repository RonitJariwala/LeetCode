class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9+7
        even_pos=(n+1)//2
        odd_pos=n//2
        even_comb=pow(5,even_pos,MOD)
        odd_comb=pow(4,odd_pos,MOD)
        return (even_comb*odd_comb)%MOD
