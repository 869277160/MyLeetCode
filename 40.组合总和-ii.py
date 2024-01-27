#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        candidates.sort()
        self.res = []
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
            for i in range(current_idx, len(candidates)):
                if i > current_idx and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                self.traverse(candidates[i+1:], current_idx, track, target)
                track.pop()
        
        
# @lc code=end

