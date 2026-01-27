from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1,cnt2=0,0
        el1,el2=float('-inf'),float('-inf')
        n=len(nums)
        for num in nums:
            if cnt1==0 and num!=el2:
                cnt1=1
                el1=num
            elif cnt2==0 and num!=el1:
                cnt2=1
                el2=num
            elif num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
            else:
                cnt1-=1; cnt2-=1
        cnt1,cnt2=0,0
        for num in nums:
            if num==el1:
                cnt1+=1
            if num==el2:
                cnt2+=1
        mini=n//3+1
        res=[]
        if cnt1>=mini:
            res.append(el1)
        if cnt2>=mini and el1!=el2:
            # Avoid adding duplicate if el1 == el2
            res.append(el2)
        # result.sort() # TC --> O(2*log2) ~ O(1);
        return res
