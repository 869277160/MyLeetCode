'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 10:14:57
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 10:36:48
FilePath: \Leetcode_Solver\2007.从双倍数组中还原原数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#

# @lc code=start
# class Solution:
#     def findOriginalArray(self, changed: List[int]) -> List[int]:
        
#         if len(changed) % 2 == 1:
#             return []
#         else :
#             res = []
            
#             changed = sorted(changed)
#             for i in range(len(changed)):
#                 if 2*changed[i] in changed:
#                 # if i*2 in changed:
#                     res.append(changed[i])
#                     changed.remove(changed[i])
#                     changed.remove(2*changed[i])
                   
#                 else:
#                     return []
#             return res 
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        import collections
        
        changed.sort()
        res, cnts = [], collections.Counter(changed)
        for x in changed:
            if cnts[x] > 0:
                # 注意只有当计数仍大于0的话才判断, 否则说明已经被作为一个2倍数字用掉了
                if cnts[2 * x] <= 0 or x == 0 and cnts[x] < 2:
                    # 如果二倍数字不存在, 或者当前数字是0且计数小于2, 肯定不可能是双倍数组
                    return []
                # x属于原数组
                res.append(x)
                cnts[x] -= 1
                cnts[2 * x] -= 1
        return res



        #     for i in changed:
        #         if i*2 in changed:
        #             res.append(i)
        #             changed.remove(i)
        #             changed.remove(i*2)
        #         else:
        #             return []
        
        # return res
# @lc code=end

