from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_counts = Counter(hand)
        for card in sorted(card_counts.keys()):
            count = card_counts[card]
            if count > 0:
                for i in range(groupSize):
                    if card_counts[card + i] < count:
                        return False
                    card_counts[card + i] -= count
                    
        return True