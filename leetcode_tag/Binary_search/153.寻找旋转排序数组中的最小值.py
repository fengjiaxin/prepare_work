# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
#
# 请找出其中最小的元素。

# 1 <= nums.length <= 5000
# -5000 <= nums[i] <= 5000
# nums 中的所有整数都是 唯一 的
# nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转

class Solution:
    def findMin(self, nums):
        # 所有数字都是唯一的，
        # 其实就是找到两个升序范围的交叉点
        left = 0
        right = len(nums) - 1
        # 在[left,right]进行搜索
        if nums[left] <= nums[right]:
            return nums[left]
        while left < right:
            if right - left == 1:
                return nums[right]
            mid = left + (right - left)//2
            if nums[mid] >= nums[left]:
                left = mid
            if nums[mid] <= nums[right]:
                right = mid

nums = [4,5,6,7,0,1,2]
s = Solution()
res = s.findMin(nums)
print(res)