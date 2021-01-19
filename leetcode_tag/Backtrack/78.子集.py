# 给你一个整数数组 nums ，返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。

class Solution:
    def subsets(self, nums):
        length = len(nums)
        res = []

        # 这个题的思路就是，对于每个元素，有两种选择，用或者不用
        # path:已经走过得路径 index代表第index个元素
        def helper(path,index):
            if index == length:
                res.append(path.copy())
                return
            # 不选择第index个元素
            helper(path,index+1)
            # 选择第index个元素
            path.append(nums[index])
            helper(path,index+1)
            path.pop(-1)
        helper([],0)
        return res

s = Solution()
nums = [1,2,3]
res = s.subsets(nums)
print(res)