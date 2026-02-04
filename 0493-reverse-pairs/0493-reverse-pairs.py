class Solution:

    def merge(self,a,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if a[left]<=a[right]:
                temp.append(a[left])
                left+=1
            else:
                temp.append(a[right])
                right+=1
        while left<=mid:
            temp.append(a[left])
            left+=1
        while right<=high:
            temp.append(a[right])
            right+=1
        for i in range(low,high+1):
            a[i]=temp[i-low]

    def countPairs(self,a,low,mid,high):
        cnt=0
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and a[i]>2*a[right]:
                right+=1
            cnt+=(right-(mid+1))
        return cnt

    def mergeSort(self,a,low,high):
        cnt=0
        if low>=high: return cnt
        mid=(low+high)//2
        cnt+=self.mergeSort(a,low,mid)
        cnt+=self.mergeSort(a,mid+1,high)
        cnt+=self.countPairs(a,low,mid,high)
        self.merge(a,low,mid,high)
        return cnt


    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)