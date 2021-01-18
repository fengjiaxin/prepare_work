# 升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
#
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 提示：
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4 <= target <= 10^4

class Solution:
    def search(self, nums, target):
        length = len(nums)
        left = 0
        right = length - 1
        # nums中的每个数值都不一样
        # 搜索区间为闭区间
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            # 如果[left,mid]是升序:
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else: # [mid,right]是升序
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        return -1

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 3
res = s.search(nums,target)
print(res)