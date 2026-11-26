class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        size = []
        for st in strs:
            size.append(len(st))
        ans = ','.join(map(str, size)) + '#' + ''.join(strs)
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizeSt, st = s.split('#', 1)
        size = list(map(int, sizeSt.split(',')))
        print(size)
        print(st)
        res = []
        cur = 0
        read = 0
        for l in size:
            temp = ''
            while cur < read + l:
                temp = temp + st[cur]
                cur += 1
            read = cur
            res.append(temp)
        return res