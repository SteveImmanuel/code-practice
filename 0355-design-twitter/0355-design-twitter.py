class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.user_tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.timestamp, tweetId)
        self.user_tweets[userId].append(tweet)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_heap = []
        for followee_id in self.users[userId]:
            for timestamp, tweet_id in self.user_tweets[followee_id][-10:]:
                heapq.heappush(tweet_heap, (-timestamp, tweet_id))
        
        for timestamp, tweet_id in self.user_tweets[userId][-10:]:
            heapq.heappush(tweet_heap, (-timestamp, tweet_id))
            
        res = []
        for _ in range(10):
            if len(tweet_heap) <= 0:
                break
            res.append(heapq.heappop(tweet_heap)[1])
        return res
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)