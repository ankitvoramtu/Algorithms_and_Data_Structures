def twoSum(nums, target):
    if len(nums) > 1:
        d = {}
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = nums.index(nums[i])
            else:
                return [i, d[nums[i]]]
    return None
# Time: O(n)
# Space: O(1) or O(n)?