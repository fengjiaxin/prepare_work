# 峰值元素是指其值大于左右相邻值的元素。
#
# 给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。

# 我们可以将 numsnums 数组中的任何给定序列视为交替的升序和降序序列。通过利用这一点，以及“可以返回任何一个峰作为结果”的要求，我们可以利用二分查找来找到所需的峰值元素。
#
# 在简单的二分查找中，我们处理的是一个有序数列，并通过在每一步减少搜索空间来找到所需要的数字。在本例中，我们对二分查找进行一点修改。首先从数组 numsnums 中找到中间的元素 midmid。若该元素恰好位于降序序列或者一个局部下降坡度中（通过将 nums[i]nums[i] 与右侧比较判断)，则说明峰值会在本元素的左边。于是，我们将搜索空间缩小为 midmid 的左边(包括其本身)，并在左侧子数组上重复上述过程。
#
# 若该元素恰好位于升序序列或者一个局部上升坡度中（通过将 nums[i]nums[i] 与右侧比较判断)，则说明峰值会在本元素的右边。于是，我们将搜索空间缩小为 midmid 的右边，并在右侧子数组上重复上述过程。
#
# 就这样，我们不断地缩小搜索空间，直到搜索空间中只有一个元素，该元素即为峰值元素。

class Solution:
    def findPeakElement(self, nums):
        # 时间复杂度O(n)
        # 判断元素是否在升序坡上
        length = len(nums)
        # function1
        # for i in range(length - 1):
        #     if nums[i] > nums[i+1]:
        #         return i
        # return length - 1
        def search(nums,left,right):
            if left == right:
                return left
            mid = left + (right - left)//2
            if nums[mid] > nums[mid + 1]:
                return search(nums,left,mid)
            else:
                return search(nums,mid+1,right)
        return search(nums,0,length-1)



nums = [1,2,3,1]
s = Solution()
res = s.findPeakElement(nums)
print(res)
