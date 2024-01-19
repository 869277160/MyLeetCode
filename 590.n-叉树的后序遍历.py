#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
                
        # 结果返回
        res = []
        
        # 结束条件 
        if root == None:
            return []
        if root.children == None:
            return [root.val] 
        
        # 进一步搜索
        
        for node in root.children:
            res += self.postorder(node)
        res += [root.val]
        return res 
    
# @lc code=end

