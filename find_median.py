from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -num)
            x = heappop(self.small)
            heappush(self.large, -x)
        else:
            heappush(self.large, num)
            x = heappop(self.large)
            heappush(self.small, -x)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])