class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints[:k])
        maxPoints=total
        for i in range(k):
            total-=cardPoints[k-1-i]
            total+=cardPoints[n-1-i]
            maxPoints=max(maxPoints,total)
        return maxPoints

