# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        length = len(nums)
        res = []
        # 表示处理范围为[start,length-1]
        def helper(path,start):
            res.append(path.copy())
            for i in range(start,length):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                helper(path,i+1)
                path.pop(-1)
        helper([],0)
        return res
nums = [2,1,2]
s = Solution()
res = s.subsetsWithDup(nums)
print(res)