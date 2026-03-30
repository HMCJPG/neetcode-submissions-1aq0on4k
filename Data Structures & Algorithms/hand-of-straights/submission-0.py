class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        lenHand = len(hand)
        if lenHand % groupSize != 0:
            return False

        hand.sort()

        while hand:

            first = hand[0]
            value = first
            hand.remove(first)

            for i in range(groupSize - 1):

                value += 1
                if value not in hand:
                    return False
                hand.remove(value)

        return True

        