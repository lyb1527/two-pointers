def twoSum(nums, target):
    if nums is None or len(nums) < 2:
        return 0

    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        value = nums[left] + nums[right]
        if value == target:
            count += 1
            left += 1
            right -= 1
            while left < right and nums[right] == nums[right +1]:
                right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif value > target:
            right -= 1
        else:
            left += 1

    return count


nums = [1,1,2,45,46,46, 3, 44, 4, 43, 5, 42, 6, 41]
print(twoSum(nums, 47))
