class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxInd=0,n=nums.size();
        for(int i=0;i<n;i++){
            if(i>maxInd) return false;
            maxInd=max(maxInd,i+nums[i]);
        }
        return true;
    }
};