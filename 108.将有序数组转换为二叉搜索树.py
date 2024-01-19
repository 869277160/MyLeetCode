#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # 将有序数组转换为二叉搜索树
        # 将其看作一个中序遍历
        length = len(nums)
        if length == 1 :
            return TreeNode(nums[0])
        elif length ==2 :
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = None
            return root
        else :
            if length % 2 == 1:
                root = TreeNode(nums[length//2])
                root.left = self.sortedArrayToBST(nums[:length//2])
                root.right = self.sortedArrayToBST(nums[(length//2)+1:])
                return root
            else :
                root = TreeNode(nums[length//2])
                root.left = self.sortedArrayToBST(nums[:length//2])
                root.right = self.sortedArrayToBST(nums[(length//2)+1:])
                return root
              
              
        
# @lc code=end

