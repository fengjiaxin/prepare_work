# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。

# 注意边界条件
class Solution:
    def findMin(self, nums):
        # 可能包含重复元素
        def travsrse_min(nums):
            return min(nums)
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right] or right == 0:
            return nums[left]
        while left < right:
            if right - left == 1:
                return nums[right]
            mid = left + (right - left)//2
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                return travsrse_min(nums)
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid

s = Solution()
nums = [2,2,2,0,1]
res = s.findMin(nums)
print(res)