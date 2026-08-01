import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps: 
        # small is a max-heap (inverted values) for the smaller half
        # large is a min-heap for the larger half
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. By default, push into the max-heap (small half)
        heapq.heappush(self.small, -num)
        
        # 2. Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Balance the sizes
        # If small is getting too big (more than 1 element larger than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # If large somehow gets bigger than small, move an element back
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, the median is the root of the small max-heap
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even number of elements, it's the average of the two roots
        else:
            return (-self.small[0] + self.large[0]) / 2.0