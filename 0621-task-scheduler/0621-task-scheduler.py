from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks) 
        max_freq = max(counts.values())
        max_count = sum(1 for v in counts.values() if v == max_freq)   
        calculated_intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), calculated_intervals)