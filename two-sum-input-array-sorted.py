'''
Given an array of integers that is already sorted in ascending order
find two numbers such that they add up to a specific number

NOTE: returned answers are not zero-based. Index 1 is smaller than index2

'''


class Solution():

    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                return [left + 1, right + 1]
            elif value < target:
                left += 1
            else:
                right -= 1
        return []

nums = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(nums, 9))
