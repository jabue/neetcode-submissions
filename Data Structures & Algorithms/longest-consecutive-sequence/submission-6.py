class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        dedup = set(nums)
        for num in dedup:
            if num - 1 not in dedup:
                curr = num
                length = 1
                while curr + 1 in dedup:
                    curr += 1
                    length += 1
                res = max(res, length)
        return res
                    
                

        