#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # wrong_1 = None
        # wrong_2 = None
        
        # def helper(root):
        #     if root == None :
        #         return 
        #     else :
        #         if root.left == None and root.right == None:
        #             return
        #         if root.left != None and root.right == None:
        #             return
        #         if root.left == None and root.right != None:
        #             return
        #         if root.left != None and root.right != None:
        #             if root.left.val > root.val or root.right.val < root.val:
        #                 return root
        #             return
# @lc code=end

