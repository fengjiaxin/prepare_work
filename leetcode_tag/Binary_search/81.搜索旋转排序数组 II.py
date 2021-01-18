# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
class Solution:
    def search(self, nums, target):
        # 元素有可能有重复的，有的时候无法判断
        def traverse_search(nums,target):
            for num in nums:
                if num == target:
                    return True
            return False
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                return traverse_search(nums,target)
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        return False

s = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
res = s.search(nums,target)
print(res)