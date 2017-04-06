'''
Given an array nums of integers and an int k, partition the array, that is move the
elements in nums, such that

* all elements < k are moved to the left
* all the element >= k are moved to the right

return the partitioning index, that is the first index i nums[i] = k


If nums = [3,2,2,1] and k=2, a valid answer is 1.
'''


class Solution:
    """
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
