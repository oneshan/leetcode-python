# 0355 - Design Twitter
# Date: 2024-05-29
# Runtime: 33 ms, Memory: 16.7 MB
# Submission Id: 1271087436


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)  # userId: [(ts, tweetId)]
        self.follow_list = defaultdict(set)  # userId: [userIds]
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.follow_list[userId].add(userId)
        for uid in self.follow_list[userId]:
            if uid in self.tweets:
                ts = self.tweets[uid][-1][0]
                heapq.heappush(max_heap, (-ts, 1, uid))

        while max_heap and len(res) < 10:
            _, idx, uid = heapq.heappop(max_heap)
            res.append(self.tweets[uid][-idx][1])
            if len(self.tweets[uid]) > idx:
                idx += 1
                ts = self.tweets[uid][-idx][0]
                heapq.heappush(max_heap, (-ts, idx, uid))
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