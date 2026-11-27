class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                topT, topI = stack.pop()
                res[topI] = i - topI
            stack.append((t, i))
        return res
