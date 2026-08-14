class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            if num in nums:
                complementary = target-num
            if complementary in count:
                return (count[complementary], i)
            count[num] = i