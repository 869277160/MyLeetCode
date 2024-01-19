#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def Helper(RootNode, current, Sum):
            if RootNode == None:
                return False
            current_all = current + RootNode.val
            if current_all == Sum and RootNode.left == None and RootNode.right == None:
                return True
            else :
                Left = Helper(RootNode.left, current_all, Sum)
                Right = Helper(RootNode.right, current_all, Sum)
                return Left or Right
        
                
        # if root == None:
        #     return False
        # else:
        return Helper(root, 0, targetSum)
        
# @lc code=end

