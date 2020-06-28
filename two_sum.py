class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in range(0, len(nums)):
            for item_2 in range(item+1, len(nums)):
                if nums[item] + nums[item_2] == target:
                    return [item, item_2]
