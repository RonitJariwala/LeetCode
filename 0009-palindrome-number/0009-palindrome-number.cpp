class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x%10==0 && x!=0)) return false;
        int copy=x,digit;
        long long rev=0;
        while(x!=0){
            digit=x%10;
            rev=(rev*10)+digit;
            x=x/10;
        }
        if(copy==rev) return true;
        else return false;
    }
};