# 0355 - Design Twitter
# Date: 2024-05-29
# Runtime: 41 ms, Memory: 16.8 MB
# Submission Id: 1271083473


class Twitter:

    def __init__(self):
        self.tweets = {}  # user: tweets (deque, newest first)
        self.follow_list = defaultdict(set)  # user: users
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        if len(self.tweets) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.follow_list[userId].add(userId)
        for uid in self.follow_list[userId]:
            if uid in self.tweets:
                heapq.heappush(max_heap, (-self.tweets[uid][0][0], 0, uid))

        while max_heap and len(res) < 10:
            tweet_id, idx, uid = heapq.heappop(max_heap)
            res.append(self.tweets[uid][idx][1])
            if len(self.tweets[uid]) > idx + 1:
                heapq.heappush(max_heap, (-self.tweets[uid][idx+1][0], idx+1, uid))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)