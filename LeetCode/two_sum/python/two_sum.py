# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        pass

    def two_sum(self, nums, target):
        if len(nums) <= 1:
            return None

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return None

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.two_sum(nums, target)
    print(result)
