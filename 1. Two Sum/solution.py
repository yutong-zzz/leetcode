class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, num in enumerate(nums):
            rest = target - num
            if rest in d:
                return [d[rest],idx]
            else:
                d[num] = idx