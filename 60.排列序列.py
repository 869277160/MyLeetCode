#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
from math import ceil, floor
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        #     #######  Solver 1 
        #         nums = [str(i) for i in range(1,n+1)]
        #         self.res = [ ]
        #         for i in range(len(nums)):
        #             self.backtrack(nums[:i]+nums[i+1:],[nums[i]])
        #         # print(self.res)
        #         return self.res[k-1]
                
        # def backtrack(self, nums, track):
        #     if nums == []:
        #         self.res.append("".join(track))
        #         return 

        #     for i in range(len(nums)):
        #         self.backtrack(nums[:i]+nums[i+1:],track+[nums[i]])
    
    
    
        #######  Solver 2 
            nums = [str(i) for i in range(1,n+1)]
            res = self.helper(nums, k)
            
            return "".join(res)
        
    def helper(self, nums:list, k:int) -> list:
            # print(nums,k)
            if len(nums) == 1:
                return nums
            elif len(nums) == 2:
                if k == 1:
                    return nums  
                if k == 0:
                    return nums[::-1] 
                else :
                    return nums[::-1] 
            else:
                res = [""]
                total = 1 
                for i in range(1, len(nums)):
                    total *= i

                current_idx = floor(k / total)
                if k % total == 0: current_idx -= 1
                res[-1] = nums[current_idx]
                nums.pop(current_idx)
                k = k % total if total != 1 else k - total
                res += self.helper(nums,k)
                
                return res 
        
        ###### solver 3
        # nums = [i for i in range(1,n+1)]
        # res = [0 for i in range(n)]
        # total = 1 
        # for i in range(1, n):
        #     total *= i
        #     res[-i-1] = total


        # for i in range(0, n):
        #     if res[i] == 1:
        #         current_num_idx = k - res[i]
        #     else :
        #         if k <= res[i]:
        #             current_num_idx = 0
        #         else:
        #             current_num_idx = floor(k / res[i])
        #             if k % res[i] == 0 and res[i] != 1:
        #                 current_num_idx -= 1 
        #             k =  k % res[i]
                
        #     # print(i, k, current_num_idx, nums, res)

        #     res[i] = nums[current_num_idx]
        #     nums.pop(current_num_idx)
        
        #     if len(nums) == 1:
        #         res[-1] = nums[-1]
                
        # res = [str(i) for i in res]
        # return "".join(res)
        
# @lc code=end


if __name__ == "__main__":
    

            
    s = Solution()
    
    # for i in range(3,5):
    for j in range(1,3):
        print(2,j,s.getPermutation(2,j))
