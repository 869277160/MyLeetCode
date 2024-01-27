#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return None
        if root.left == None and root.right == None:
            root.val = 0
        
        root, _ = self.traverse(root,0)
        
        return root

            
        
    def traverse(self,  root: TreeNode, current_sum:int) -> (TreeNode, int):
        
        if root == None:
            return root, current_sum
        
        root.right, current_sum = self.traverse(root.right, current_sum)
        current_sum = current_sum + root.val
        root.val = current_sum
        root.left, current_sum = self.traverse(root.left, current_sum)
        
        return root, current_sum
        
# @lc code=end

