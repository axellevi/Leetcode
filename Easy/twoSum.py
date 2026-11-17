class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for elem in range(len(nums)):
            for i in range(len(nums)):
                if i == elem:
                    continue
                result = nums[elem] + nums[i]
                if result == target:
                    return [elem, i]