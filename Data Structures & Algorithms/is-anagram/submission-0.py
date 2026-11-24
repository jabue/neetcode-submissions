class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mem = {}
        for c in s:
            mem[c] = mem.get(c, 0) + 1
        for c in t:
            if mem.get(c, 0) == 0:
                return False
            else:
                mem[c] = mem.get(c) - 1
        return True  