class Twitter:

    def __init__(self):
        self.count = 0 # maintain order of tweets (decremented each post)

        # can init to regular hashmap, would require a few more lines of code
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create a tweet for userId
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement count for minheap


    def getNewsFeed(self, userId: int) -> List[int]:
        # get 10 most recent posts from the user including themself

        res = [] # ordered starting from recent
        minHeap = [] # used to determine most recent

        # add userId, add themself
        self.followMap[userId].add(userId)
        # go through all users that userId follows
        for followeeId in self.followMap[userId]:
            # ensure tweets
            if followeeId in self.tweetMap:
                # get most recent tweet created by followeeId
                index = len(self.tweetMap[followeeId]) - 1 # "last index"
                # use unpacking to get count and tweetId
                count, tweetId = self.tweetMap[followeeId][index]
                # 4 values: key (order based on count), tweetId, 
                # followeeId (go back to list to get prev index),
                # index - 1 represents the next element
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        # go until all tweets are being displayed up until 10
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                self.tweetMap[followeeId][index] # next tweet to add to minHeap
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # make sure following
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
