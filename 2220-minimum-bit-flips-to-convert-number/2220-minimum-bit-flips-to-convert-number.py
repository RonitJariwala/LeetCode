class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num=start^goal
        cnt=0
        for i in range(32):
            cnt+=(num&1)
            num>>=1
        return cnt    