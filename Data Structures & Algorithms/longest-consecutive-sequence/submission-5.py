class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dedupe = sorted(set(nums))
        ans = 1
        temp = 1
        for i in range(1, len(dedupe)):
            if dedupe[i] == dedupe[i - 1] + 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 1
        return ans
        