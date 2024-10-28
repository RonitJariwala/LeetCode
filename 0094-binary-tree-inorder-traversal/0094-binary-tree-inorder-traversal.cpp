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
    void inOrder(TreeNode *r,vector<int> &a){
        if(r==NULL) return;
        inOrder(r->left,a);
        a.push_back(r->val);
        inOrder(r->right,a);
    }

    vector<int> inorderTraversal(TreeNode* r){
        vector<int> a;
        inOrder(r,a);
        return a;
    }
};