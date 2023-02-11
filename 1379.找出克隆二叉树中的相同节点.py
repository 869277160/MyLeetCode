#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # 结束条件
        if original == None:
            return None
        if original == target:
            return cloned
        
        # 循环bian'li
        if self.getTargetCopy(original.left, cloned.left, target) != None:
            return self.getTargetCopy(original.left, cloned.left, target)
        if self.getTargetCopy(original.right, cloned.right, target) != None:
            return self.getTargetCopy(original.right, cloned.right, target)
        # if self.getTargetCopy(original.left, cloned.left, target) == None and self.getTargetCopy(original.right, cloned.right, target) == None:
        #     return None
        
        
        
        
        
# @lc code=end

