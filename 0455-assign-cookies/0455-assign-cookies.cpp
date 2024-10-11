class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int m=s.size(),n=g.size(),l=0,r=0;
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        while(l<m && r<n){
            if(g[r]<=s[l]){
                r++;
            }
            l++;
        }
        return r;
    }
};