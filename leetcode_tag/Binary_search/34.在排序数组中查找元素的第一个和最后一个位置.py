# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。


class Solution:
    def searchRange(self, nums, target):
        # 这个问题就是找到第一个>= target的index
        length = len(nums)
        def findFirst(nums,target):
            left = 0
            right = length
            while left < right:
                mid = left + (right - left)//2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        first = findFirst(nums,target)
        if first < length and nums[first] == target:
            end = findFirst(nums,target + 1)
            return [first,end - 1]
        else:
            return [-1,-1]

s = Solution()
nums = [5,7,7,8,8,10]
target = 6
res = s.searchRange(nums,target)
print(res)