#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:

        # 位数（一位数，两位数...）
        digit = 1
        # 1,10,100, 1000 这样的后缀
        base = 1

        while n > 9 * base * digit:
            n -= 9 * base * digit
            base *= 10
            digit += 1

        # 此时假设 base = 1000，那么说明 n 是 100~999 中的某个三位数的某一位
        # 哪个三位数呢？这样算：
        val = base + (n - 1) // digit
        # 是这个三位数的第几位呢？这样算：
        index = (n - 1) % digit

        # 怎么把 val 的第 index 这一位数字抠出来呢？可以转化成字符串来算：
        return int(str(val)[index])
# @lc code=end

