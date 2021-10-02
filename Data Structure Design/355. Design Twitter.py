355. Design Twitter

class Tweet:
    def __init__(self, id_, post_time_):
        self.id = id_
        self.post_time = post_time_
        self.next_tweet = None

class User:
    def __init__(self, user_id_):
        self.user_id = user_id_
        # 每个用户的关注列表在自己的实例中维护
        # Users always follower themselves
        self.followed_list = set([user_id_])
        # 每个用户的推文链在自己的实例中维护
        # 用来指向推文链表的头节点
        self.post_list = None

    def follow(self, user_id_):
        self.followed_list.add(user_id_)


    def unfollow(self, user_id_):
        if user_id_ != self.user_id:
            self.followed_list.discard(user_id_)
        
    def postTweet(self, tweetID, post_time_):
        new_tweet = Tweet(tweetID, post_time_)
        new_tweet.next_tweet = self.post_list
        self.post_list = new_tweet
        

class Twitter:

    def __init__(self):
        self.timestamp = 0
        # userId 映射到 User 对象
        self.user_dict = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 若 userId 是新 id，新建一个 User 类
        if not userId in self.user_dict:
            self.user_dict[userId] = User(userId)
        self.user_dict[userId].postTweet(tweetId, self.timestamp)
        self.timestamp += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        # 根据题目示例，关注 API 也可以新建用户，不论是发起关注还是被关注
        if not followerId in self.user_dict:
            self.user_dict[followerId] = User(followerId)

        if not followeeId in self.user_dict:
            self.user_dict[followeeId] = User(followeeId)
        
        self.user_dict[followerId].follow(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_dict:
            self.user_dict[followerId].unfollow(followeeId)


    def getNewsFeed(self, userId: int) -> List[int]:
        # 用 heapq 实现k个有序链表合并，这里看出来也可以用列表实现
        from heapq import heappop, heappush, heapify
        res = []
        help_list = []
        heapify(help_list)
        if not userId in self.user_dict: return res

        # 用户的关注列表，不会为空，至少有他自己
        user_follow_list = self.user_dict[userId].followed_list
        # followee 是 userId 
        for uid in user_follow_list:
            followee = self.user_dict[uid]
            if not followee.post_list: continue
            heappush(help_list, (followee.post_list.post_time*(-1), followee.post_list))

        while help_list:
            if len(res) >= 10: break
            _, tt = heappop(help_list)
            res.append(tt.id)
            if tt.next_tweet:
                heappush(help_list, (tt.next_tweet.post_time*(-1), tt.next_tweet))

        return res


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)