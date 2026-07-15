class Twitter:

    def __init__(self):
        self.tweetMap=defaultdict(list)
        self.followMap=defaultdict(set)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweetMap[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap=[]
        users={userId} | self.followMap[userId]
        for i in users:
            info=self.tweetMap[i][-10:]
            for t,i in info:
                heapq.heappush(maxHeap,(-t,i))
        result=[]
        for i in range(10):
            if len(maxHeap)==0:
                return result
            pop=heapq.heappop(maxHeap)
            result.append(pop[1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
