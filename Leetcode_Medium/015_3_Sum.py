'''
15. 3Sum 

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) <= 2:
        	return ret # ret is []
        nums.sort()
        i = len(nums) - 1
        while i > 2:
        	if i < len(nums) - 1 and nums[i] = nums[i + 1]:
        		continue
        	cur_ret = self.two_sum(num, i - 1, - nums[i])
        	ret.append(cur_ret)





        	i = i - 1
