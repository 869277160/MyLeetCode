'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 23:01:25
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 23:55:31
FilePath: \Leetcode_Solver\39.组合总和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 23:01:25
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 23:25:25
FilePath: \Leetcode_Solver\39.组合总和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    '''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-23 23:01:25
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-23 23:26:29
FilePath: \Leetcode_Solver\39.组合总和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        # self.track = []
        # self.trackSum = 0
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        self.traverse(candidates, 0, [], target)
        return self.res
    
    def traverse(self,candidates: List[int], current_idx: int, track: List[int], target: int):
        # print(candidates, current_idx)
        # print(track, sum(track))
        trackSum = sum(track)
        if trackSum == target:
            self.res.append(list(track))
            return
        elif trackSum > target:
            return
        elif trackSum < target:
            for num in candidates[current_idx:]:
                track.append(num)
                self.traverse(candidates, current_idx, track, target)
                current_idx += 1 
                track.pop()
# @lc code=end

