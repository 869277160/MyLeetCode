#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        
        res = self.levelOrderhelper(root=root, level=0, res=[[]])
        
        res = [sum(i)/len(i) for i in res]
        
        return res 
 
    def levelOrderhelper(self,root, level=0, res=[[]]):
        # 返回原有结果即可
        if root == None:
            return res 
        # 判断是否是新的一层
        if len(res) == level:
            res.append([])
            
        # 类似先序遍历，先自己，之后左右，每一层的值都是物理上从左到右的。
        res[level].append(root.val)
        res = self.levelOrderhelper(root.left, level+1, res)
        res = self.levelOrderhelper(root.right, level+1, res)
        
        return res 

        
        
# @lc code=end

