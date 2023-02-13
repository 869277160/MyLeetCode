#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # 直接返回
        if nums1 == []:
            nums1 = nums2
            return 
        if nums2 == []:
            return

        
        # 双指针
        p1, p2 = 0,0
        
        while(p1<(m+n) and p2 < n):
            
            if nums1[p1] >= nums2[p2]:
                temp = nums1[p1]
                nums1[p1] = nums2[p2]
                nums1[p1+1] = temp
                nums1[p1+1:] = nums1[p1+1:-1]
                
                p2 +=  1
                
            if nums1[p1] < nums2[p2] or p2 == len(nums2):
                p1 += 1
        
        return
# @lc code=end

