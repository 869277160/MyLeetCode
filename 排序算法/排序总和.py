'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-31 13:20:31
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-31 13:34:30
FilePath: \Leetcode_Solver\排序算法\排序总和.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from typing import List
class Solver:
    def __init__(self) -> None:
        pass
    
    # 插入排序_1 冒泡排序
    def bubbleSort(self, nums: List[int]) -> List[int]:
        
        pass 
        
    # 插入排序_1 快速排序
    def quickSort(self, nums: List[int]) -> List[int]:
        
        return self.quickSortBetween(nums, 0, len(nums) - 1)
    
    def quickSortBetween(self, nums: List[int], low: int, high: int) -> List[int]:
                
        if low < high :
            pivot_pos = self.partitionForQuickSort(nums, low, high)
            self.quickSortBetween(nums, low, pivot_pos - 1)
            self.quickSortBetween(nums, pivot_pos + 1,high)
        return nums
        
    def partitionForQuickSort(self, nums: List[int], low: int, high: int) -> int:
        
        pivots = nums[low]
        while(low< high):
            while (low<high) and (nums[high] >= pivots):
                high-=1
            nums[low] = nums[high]
            
            while (low<high) and (nums[low] <= pivots):
                low+=1
            nums[high] = nums[low]
        
        nums[low] = pivots
        
        return low



if __name__ == "__main__":
    
    s = Solver()
    input = [3,6,8,5,7,2,4,1,5]
    output = s.quickSort(input)
    
    print(output)