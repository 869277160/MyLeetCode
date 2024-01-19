#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def get_level_ordered_tree(current_root, level,res) -> list:
            if not current_root:
                return res
            if level == len(res):
                res.append([])
            
            # if level <= len(res):
            res[level].append(current_root.val)
            
            # if the left node is not empty, then we need to traverse it.
            if current_root.left:
                get_level_ordered_tree(current_root.left, level + 1, res)
            if current_root.right:
                get_level_ordered_tree(current_root.right,level + 1, res)
            
            return res 
            # get_right_vision(root.right, level + 1, res)
            # get_right_vision(root.left, level + 1, res)
        
        ordered_res = get_level_ordered_tree(current_root=root,level=0,res=[])
        
        print(ordered_res)
        
        right_vision = [res[-1] for res in ordered_res]
        
        return right_vision
        
        
# @lc code=end

