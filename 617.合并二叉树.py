#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 遍历所有可能的情况进行迭代
        if root1 == None and root2 == None: 
            return None 
        if root1 == None and root2 != None: 
            return root2
        if root1 != None and root2 == None: 
            return root1
        if root1 != None and root2 != None: 
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left,root2.left)
            res.right = self.mergeTrees(root1.right,root2.right)
            return res

# @lc code=end

