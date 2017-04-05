'''
Given an array nums of n integers, find two integers in nums such that the
sum is cloest to a given number, target
Return the difference between the sum of the two integers and the target

Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

'''
class Solution:

    # return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):

        nums.sort()
        i, j = 0, len(nums)  - 1

        diff = 0x7fffffff
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1

        return diff
