# 给定两个数组，编写一个函数来计算它们的交集。
# 思路：给两个数组排序，然后遍历
class Solution:
    def intersection(self, nums1, nums2):
        # 核心就是对两个数组排序
        nums1.sort()
        nums2.sort()
        res = []
        length1 = len(nums1)
        length2 = len(nums2)
        index1 = 0
        index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] == nums2[index2]:
                if len(res) == 0 or nums1[index1] != res[-1]:
                    res.append(nums1[index1])
                index1 += 1
                index2 += 1

            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return res

nums1 = [1,2,2,1]
nums2 = [2,2]
s = Solution()
res = s.intersection(nums1,nums2)
print(res)