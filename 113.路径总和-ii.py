#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        if root == None:
            return res
        
        # def Helper(RootNode, Current, Sum=targetSum, CurrentPath=[]):
            # if RootNode == None:
            #     return 
            
            # Current_all = Current + RootNode.val
            # # CurrentPath.append(RootNode.val)
            # if Current_all == Sum and RootNode.left == None and RootNode.right == None:
            #     CurrentPath.append(RootNode.val)
            #     res.append(CurrentPath)
            #     return 
            # if Current_all == Sum and RootNode.left == None and RootNode.right != None:
            #     return
            # if Current_all == Sum and RootNode.left != None and RootNode.right == None:
            #     return
            # if Current_all == Sum and RootNode.left != None and RootNode.right != None:
            #     left_path = CurrentPath + [RootNode.val]
            #     right_path = CurrentPath + [RootNode.val]
            #     Helper(RootNode.left, Current_all, Sum, left_path)
            #     Helper(RootNode.right, Current_all, Sum, right_path)
            #     return 
                
            # if Current_all != Sum and RootNode.left == None and RootNode.right == None:
            #     return 
            # if Current_all != Sum and RootNode.left == None and RootNode.right != None:
            #     CurrentPath.append(RootNode.val)
            #     Helper(RootNode.right, Current_all, Sum, CurrentPath)
            #     return
            # if Current_all != Sum and RootNode.left != None and RootNode.right == None:
            #     CurrentPath.append(RootNode.val)
            #     Helper(RootNode.left, Current_all, Sum, CurrentPath)
            #     return
            # if Current_all != Sum and RootNode.left != None and RootNode.right != None:
            #     # left_path = CurrentPath.append(RootNode.val)
            #     # right_path = CurrentPath.append(RootNode.val)
            #     left_path = CurrentPath + [RootNode.val]
            #     right_path = CurrentPath + [RootNode.val]
            #     Helper(RootNode.left, Current_all, Sum, left_path)
            #     Helper(RootNode.right, Current_all, Sum, right_path)
            #     return 
        
        
        
        def Helper(RootNode, Current, CurrentPath=[]):
            # if RootNode == None:
            #     return 
            
            Current = Current + RootNode.val
            # CurrentPath.append(RootNode.val)
            if Current == targetSum and RootNode.left == None and RootNode.right == None:
                CurrentPath.append(RootNode.val)
                res.append(CurrentPath)
                return 
            if Current != targetSum and RootNode.left == None and RootNode.right == None:
                return 
            
            if RootNode.left != None:
                left_path = CurrentPath + [RootNode.val]
                Helper(RootNode.left, Current, left_path)
            if RootNode.right != None:
                right_path = CurrentPath + [RootNode.val]
                Helper(RootNode.right, Current, right_path)
            return

            # if Current == Sum and RootNode.left == None and RootNode.right != None:
            #     return
            # if Current_all == Sum and RootNode.left != None and RootNode.right == None:
            #     return
            # if Current_all == Sum and RootNode.left != None and RootNode.right != None:
            #     left_path = CurrentPath + [RootNode.val]
            #     right_path = CurrentPath + [RootNode.val]
            #     Helper(RootNode.left, Current_all, Sum, left_path)
            #     Helper(RootNode.right, Current_all, Sum, right_path)
            #     return 
                
            # if Current_all != Sum and RootNode.left == None and RootNode.right == None:
            #     return 
            # if Current_all != Sum and RootNode.left == None and RootNode.right != None:
            #     CurrentPath.append(RootNode.val)
            #     Helper(RootNode.right, Current_all, Sum, CurrentPath)
            #     return
            # if Current_all != Sum and RootNode.left != None and RootNode.right == None:
            #     CurrentPath.append(RootNode.val)
            #     Helper(RootNode.left, Current_all, Sum, CurrentPath)
            #     return
            # if Current_all != Sum and RootNode.left != None and RootNode.right != None:
            #     # left_path = CurrentPath.append(RootNode.val)
            #     # right_path = CurrentPath.append(RootNode.val)
            #     left_path = CurrentPath + [RootNode.val]
            #     right_path = CurrentPath + [RootNode.val]
            #     Helper(RootNode.left, Current_all, Sum, left_path)
            #     Helper(RootNode.right, Current_all, Sum, right_path)
            #     return 
        # if root == None:
        #     return False
        # else:
        Helper(root, 0)
        
        return res
        
        
# @lc code=end

