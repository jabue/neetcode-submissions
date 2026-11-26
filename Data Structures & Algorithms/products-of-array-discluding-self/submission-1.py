class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
                right[len(nums) - i - 1] = 1
            else:
                left[i] = left[i - 1] * nums[i - 1]
                right[len(nums) - i - 1] = right[len(nums) - i] * nums[len(nums) - i]
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res