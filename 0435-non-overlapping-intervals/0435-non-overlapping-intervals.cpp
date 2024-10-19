class Solution {
public:
    static bool comparator(vector<int>& interval1,vector<int>& interval2){
        return interval1[1]<interval2[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),comparator);
        int count=0,prevEnd=intervals[0][1];
        for(int i=1;i<intervals.size();i++){
            if(intervals[i][0]<prevEnd) count++;
            else prevEnd=intervals[i][1];
        }
        return count;
    }
};