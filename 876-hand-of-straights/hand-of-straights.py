class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        from collections import defaultdict
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        count=defaultdict(int)
        for h in hand:
            count[h]+=1
        for card in hand:
            if count[card]==0:
                continue
            for i in range(groupSize):
                curr=card+i
                if curr not in count or count[curr]==0:
                    return False
                count[curr]-=1
        return True