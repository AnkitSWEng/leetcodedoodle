'''
Given : Array of integers and target
Output : Indices of the two numbers whose sum equals to target.
Constraints :Each array has one solution, can not use the same element twice.
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_dict = {}
        for counter , value in enumerate(nums):
            difference = target - value
            
            if difference in index_dict:
                return [index_dict[difference], counter]
            else:
                index_dict[value] = counter
            