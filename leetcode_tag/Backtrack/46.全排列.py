# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

class Solution:
    def permute(self, nums):
        res = []
        def helper(path,lefts):
            length = len(lefts)
            if length == 0:
                res.append(path.copy())
                return
            for i,n in enumerate(lefts):
                path.append(n)
                helper(path,lefts[:i] + lefts[i+1:])
                path.pop(-1)
        helper([],nums)
        return res

nums = [1,2,3]
s = Solution()
res = s.permute(nums)
print(res)