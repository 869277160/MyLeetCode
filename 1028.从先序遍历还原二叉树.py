#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        if traversal == "":
            return None
        else:
            if traversal[0] != "-":
                current_val = int(traversal.split("-")[0])
                current_node = TreeNode(current_val)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
# @lc code=end

