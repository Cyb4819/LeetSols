class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i, num in enumerate(nums):
            if num in count:
                return True
            else:
                count[num]=1
        return False
        