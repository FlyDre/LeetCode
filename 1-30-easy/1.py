
"""
 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 你可以按任意顺序返回答案。
"""

# 方法一：暴力解法 时间复杂度:O(n^2), 空间复杂度:O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break
            if res != []:
                break

        return res


# 方法二： 排序+双指针 时间复杂度:O(nlogn), 空间复杂度:O(n) (先将数组排序好O(nlogn)，再利用双指针法遍历一遍O（n）得到结果)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        temp.sort()  # no return, directly changes variable 'temp'  O(nlogn)
        i = 0
        j = len(nums)-1
        while i < j:
            if (temp[i]+temp[j]) > target:
                j = j-1
            elif (temp[i]+temp[j]) < target:
                i = i+1
            else:
                break
        p = nums.index(temp[i])  # find index of value:temp[i]
        # remove the first element whose value equals temp[i], in order to avoid the case of same elements.
        # e.g. input: nums:[3, 3], target:6, without nums.pop(p), returns [0, 0], but truth is [0, 1]
        nums.pop(p)
        k = nums.index(temp[j])  #
        if k >= p:
            k = k+1
        return [p, k]


# 方法三： Hash 时间复杂度:O(n), 空间复杂度:O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target - nums[i]) is not None:
                return [hashset.get(target-nums[i]), i]
            hashset[nums[i]] = i


