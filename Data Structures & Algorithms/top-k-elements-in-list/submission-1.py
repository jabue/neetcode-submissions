class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        countSorted = dict(sorted(count.items(), key = lambda item:item[1], reverse = True))
        return list(countSorted.keys())[:k]
