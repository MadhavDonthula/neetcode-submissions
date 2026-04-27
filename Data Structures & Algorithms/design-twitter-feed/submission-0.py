from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.follower_to_followee = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1 
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        all_Users = self.follower_to_followee[userId].copy()
        all_Users.add(userId)
        minHeap = []
        for uId in all_Users:
            for ts, tId in self.tweets[uId]: 
                heapq.heappush(minHeap, (-ts, tId))
        res = []
        count = 10
        while minHeap and count > 0: 
            neg_ts, tId = heapq.heappop(minHeap)
            res.append(tId)
            count -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follower_to_followee[followerId]:
            return None
        self.follower_to_followee[followerId].remove(followeeId)
