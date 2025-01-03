/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxi=0;
    int diameterOfBinaryTree(TreeNode* r) {
        findHeight(r);
        return maxi;
    }
    int findHeight(TreeNode *r){
        if(r==nullptr) return 0;
        int lh=findHeight(r->left);
        int rh=findHeight(r->right);
        maxi=max(maxi,rh+lh);
        return 1+max(lh,rh);
    }
};