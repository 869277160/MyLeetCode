#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        for i in range(len(image)):
            res.append([1-image[i][::-1][j] for j in range(len(image[0]))])
            # print(res)

        return res 
        
        
        
# @lc code=end

