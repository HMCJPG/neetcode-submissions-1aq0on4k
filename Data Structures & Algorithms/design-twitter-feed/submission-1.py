from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        self.follows[userId].add(userId)

        heap = []
        
        for followee in self.follows[userId]:
            for ts, tid in self.tweets[followee]:

                heapq.heappush(heap, (ts, tid))

                if len(heap) > 10:
                    heapq.heappop(heap)

        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
