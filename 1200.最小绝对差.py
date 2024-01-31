#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        temp_dict = {}
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] not in temp_dict.keys():
                temp_dict[arr[i] - arr[i-1]] = []
            temp_dict[arr[i] - arr[i-1]].append([arr[i-1],arr[i]])
        
        return temp_dict[min(temp_dict.keys())]
        
# @lc code=end

