#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
                
        # (1) 后序遍历是左右中
        # 
        
        # 结果返回
        res = []
        
        # 结束条件 
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val] 
        
        # 进一步搜索
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res += [root.val]


        return res 
        
# @lc code=end

