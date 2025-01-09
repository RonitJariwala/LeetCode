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
    void inOrder(TreeNode *node,int &count,int k,int &kSmallest){
        if(!node||count>=k) return;
        inOrder(node->left,count,k,kSmallest);
        count++;
        if(count==k){
            kSmallest=node->val;
            return;
        } 
        inOrder(node->right,count,k,kSmallest);
    }
    int kthSmallest(TreeNode* root, int k) {
        int cnt=0;
        int kSmallest=-1;
        inOrder(root,cnt,k,kSmallest);
        return kSmallest;
    }
};