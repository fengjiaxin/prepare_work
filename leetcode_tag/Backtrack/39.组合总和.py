# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        length = len(candidates)
        # 每次选择只能是比自己大的元素
        # first 代表选择范围为[first:]
        def helper(path,left_sum,first):
            if left_sum < 0:
                return
            elif left_sum == 0:
                res.append(path.copy())
            else:
                for i in range(first,length):
                    ca = candidates[i]
                    if ca <= left_sum:
                        path.append(ca)
                        helper(path,left_sum - ca,i)
                        path.pop(-1)
        helper([],target,0)
        return res
candidates = [2,3,6,7]
target = 7
s = Solution()
res = s.combinationSum(candidates,target)
print(res)