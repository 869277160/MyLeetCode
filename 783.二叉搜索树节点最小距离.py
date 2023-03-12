#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return -1

        if root.left == None and root.right == None:
            return -1
        
        elif root.left != None and root.right == None:
            if root.val - root.left.val == 1 :
                return 1 
            else :
                left_min = self.Findmin(root,root.val - root.left.val)
                return left_min

        elif root.left == None and root.right != None: 
            if root.right.val-root.val == 1 :
                return 1 
            else :
                right_min = self.Findmin(root,root.right.val-root.val)
                return right_min
        
        elif root.left != None and root.right != None:
            current_left_min = root.val - root.left.val
            current_right_min =root.right.val-root.val
            current_min = min(current_left_min,current_right_min)
            if current_min == 1:
                return 1
            else :
                left_min = self.Findmin(root,current_min)
                right_min = self.Findmin(root,current_min)
                
                return min(left_min,right_min)
        
    def Findmin(self,root,current_min):
        if root == None:
            return current_min
        
        if root.left == None and root.right == None:
            return current_min
        
        elif root.left != None and root.right == None:
            if root.left.val-root.val == 1:
                return 1
            else :
                current_left_min = min(current_min,root.val - root.left.val)
                left_min = self.Findmin(root,current_left_min)
                return left_min

        elif root.left == None and root.right != None: 
            if root.right.val-root.val == 1:
                return 1
            else:
                current_right_min = min(current_min,root.right.val-root.val)
                right_min = self.Findmin(root,current_right_min)
                return right_min
        
        elif root.left != None and root.right != None:
            current_left_min = root.val - root.left.val
            current_right_min =root.right.val-root.val
            current_min = min(current_min,current_left_min,current_right_min)
            
            if current_min == 1 :
                    return 1
            else :

                left_min = self.Findmin(root,current_min)
                right_min = self.Findmin(root,current_min)
                
                return min(left_min,right_min)
        
        
# @lc code=end

