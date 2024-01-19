#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#

# @lc code=start
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        filename_dict = {"":[]}

        res = []
        for name in names:
            if name not in res:
                res.append(name)
                filename_dict[name] = []
                filename_dict[name].append(0)
            else:
                
        
        
        
        
        
        
# @lc code=end

