#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        l_res = self.largestValues(root.left)
        r_res = self.largestValues(root.right)
        res = [root.val]
        if l_res == [] and r_res == []:
            return res
        elif l_res != [] and r_res != []:
            min_len = min(len(l_res), len(r_res))
            for i in range(min_len):
                res.append(max(l_res[i], r_res[i]))
            res += l_res[min_len:]
            res += r_res[min_len:]
            print(root.val , l_res, r_res, res)
            return res 
        else:
            return res+l_res if l_res != [] else res+r_res
            
        
# @lc code=end

