#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        if root.left == None and root.right == None: return [[root.val]]
        
        # 自身为-1位置，之后每层对应位置在level-1
        return self.levelOrderBottomHelper(root,-1,[])
        
        
    def levelOrderBottomHelper(self,root, level_index, res:list):
        if root == None: return res
        
        if -level_index > len(res):
            res.insert(0,[])
        
        if root.left == None and root.right == None: 
            res[level_index].append(root.val)
            return res
        if root.left != None and root.right == None: 
            res[level_index].append(root.val)
            res = self.levelOrderBottomHelper(root.left, level_index-1, res)
            return res
        if root.left == None and root.right != None: 
            res[level_index].append(root.val)
            res = self.levelOrderBottomHelper(root.right, level_index-1, res)
            return res
        if root.left != None and root.right != None: 
            res[level_index].append(root.val)
            res = self.levelOrderBottomHelper(root.left, level_index-1, res)
            res = self.levelOrderBottomHelper(root.right, level_index-1, res)
            return res
            
            
            
# @lc code=end

