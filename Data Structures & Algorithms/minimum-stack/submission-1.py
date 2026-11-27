class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        elm = self.stack.pop()
        self.heap.remove(elm)
        heapq.heapify(self.heap)
        return elm

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
