# leetcode 209  https://leetcode.cn/problems/minimum-size-subarray-sum/description/

# 滑动窗口法
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, result, sums = 0, float('inf'),0  # float('inf')表示无穷大，常用来比较
        for right in range(0, len(nums)):  #这个循环控制终止指针，最外层循环          
            sums += nums[right]                        
            while sums >= target:  # 这个循环控制窗口大小的变化，可以起到缩小窗口的作用             
                result = min(result, right - left + 1)
                sums -= nums[left]
                left += 1
            right += 1
        return result if result != float('inf') else 0
