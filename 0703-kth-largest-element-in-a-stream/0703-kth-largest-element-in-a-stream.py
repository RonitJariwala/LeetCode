import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        # Transform the initial list into a valid min-heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # Remove the smallest elements until only the top k remain
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new test score to the heap
        heapq.heappush(self.min_heap, val)
        
        # If adding the new score pushed our heap size over k, evict the smallest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The k-th largest element is always sitting at the root of the min-heap
        return self.min_heap[0]