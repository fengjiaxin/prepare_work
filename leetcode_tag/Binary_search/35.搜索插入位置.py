# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。

class Solution:
    def searchInsert(self, nums, target):
        # 目标变成找到第一个 >= target的index
        length = len(nums)
        # 在[)区间查询
        left = 0
        right = length
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
nums = [1,3,5,6]
target = 7
res = s.searchInsert(nums,target)
print(res)