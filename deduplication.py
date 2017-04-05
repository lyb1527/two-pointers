'''
Given an array of integers, remove the duplicate numbers in it.

1. do it in-place
2. move unique numbers to the front of the array
3. return the total number of unique number

'''

def deDuplication(nums):
    if len(nums) == 0:
        return 0

    nums.sort()
    length = 0
    for value in nums:
        if nums[value] != nums[length]:
            nums[length++] = nums[value]
