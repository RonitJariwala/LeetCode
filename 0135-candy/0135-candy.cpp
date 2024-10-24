class Solution {
public:
    int candy(vector<int>& ratings) {
        int sum=1,i=1,n=ratings.size();
        while(i<n){
            if(i<n && ratings[i]==ratings[i-1]){  //If same rating,give 1 candy and move to  the next
                sum++;
                i++;
                continue;
            }
            int peak=1;
            while(i<n && ratings[i]>ratings[i-1]){  // Moving upward, increase the candy count
                peak++;
                sum+=peak;
                i++;
            }
            int down=0;
            while(i<n && ratings[i]<ratings[i-1]){ // Moving downward, increase the candy count
                down++;
                sum+=down;
                i++;
            }
            if(down>=peak){
                sum+=down-peak+1;
            }
        }
        return sum;
    }
};
