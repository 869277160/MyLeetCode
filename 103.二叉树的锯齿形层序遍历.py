#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if root == None:
            return []
        if root.left == None and root.right == None:
            return[[root.val]]
        
        res = self.levelOrderhelper(root=root, level=0, res=[[]])
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        
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

