class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                smaller_el=stack.pop()
                nge_map[smaller_el]=num
            stack.append(num)
        for num in stack:
            nge_map[num]=-1
        ans=[]
        for num in nums1:
            ans.append(nge_map[num])
        return ans