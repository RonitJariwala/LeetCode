class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:   
        xorr=0
        for num in nums:
            xorr^=num
        # find rightmost bit
        mask=xorr & (-xorr)
        # bucket of 0 and 1
        b1=0
        b2=0
        # check set bit
        for num in nums:
            if num & mask:
                b1^=num
            else:
                b2^=num
        return [b1,b2]
