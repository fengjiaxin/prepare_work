# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        def helper(path,lefts):
            length = len(lefts)
            if length == 0:
                res.append(path.copy())
                return
            for i in range(length):
                if i > 0 and lefts[i] == lefts[i-1]:
                    continue
                path.append(lefts[i])
                helper(path,lefts[:i] + lefts[i+1:])
                path.pop(-1)
        helper([],nums)
        return res

nums = [1,1,2]
s = Solution()
res = s.permuteUnique(nums)
print(res)