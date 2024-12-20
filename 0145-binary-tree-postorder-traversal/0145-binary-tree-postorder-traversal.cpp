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
    void postOrder(TreeNode *r,vector<int> &a){
        if(r==NULL) return;
        postOrder(r->left,a);
        postOrder(r->right,a);
        a.push_back(r->val);
    }

    vector<int> postorderTraversal(TreeNode* r) {
        vector<int> a;
        postOrder(r,a);
        return a;
    }
};