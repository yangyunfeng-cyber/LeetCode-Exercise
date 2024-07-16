# leetcode 977   https://leetcode.cn/problems/squares-of-a-sorted-array/description/

# （版本一）双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, i = 0, len(nums)-1, len(nums)-1
        result = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2: # 左右边界进行对比，找出最大值
                result[i] = nums[right] ** 2
                right -= 1 # 右指针往左移动
            else:
                result[i] = nums[left] ** 2
                left += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return result
