class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        countSorted = dict(sorted(count.items(), key = lambda item:item[1], reverse = True))
        heap = []
        for key, value in countSorted.items():
            heapq.heappush_max(heap, (value, key))
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res
