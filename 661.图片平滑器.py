'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 10:10:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 10:25:26
FilePath: \Leetcode_Solver\661.图片平滑器.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        res = []
        for i in range(len(img)):
            temp_res = []
            for j in range(len(img[0])):
                temp_res.append(self.getValue(img,i,j))
            res.append(temp_res)
            
        return res 
    
    def getValue(self, img:List[List[int]], i:int, j:int) -> int:
        
        around = [img[i][j]]
        
        # 上一层 
        if i-1 >= 0 and j-1 >=0: around.append(img[i-1][j-1]) 
        if i-1 >= 0: around.append(img[i-1][j])
        if i-1 >= 0 and j+1 < len(img[0]): around.append(img[i-1][j+1])

        # 本层
        if j-1 >= 0: around.append(img[i][j-1])
        if j+1 < len(img[0]): around.append(img[i][j+1])
        
        # 下一层
        if i+1 < len(img) and j-1 >= 0: around.append(img[i+1][j-1])
        if i+1 < len(img): around.append(img[i+1][j])
        if i+1 < len(img) and j+1 < len(img[0]): around.append(img[i+1][j+1])
        
        
        return sum(around) // len(around)
        
# @lc code=end

