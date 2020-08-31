# -*-coding: utf-8 -*-

class Solution:
    def __init__(self):
        pass

    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 18
    result = s.two_sum(nums, target)
    print(result)