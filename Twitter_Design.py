import heapq 
from collections import defaultdict 

class Twitter:
  def __init__(self):
    self.time = 0 
    self.following = defaultdict(set)
    self.tweets = defaultdict(list)
  
  def postTweet(self, userId, tweetId):
    self.time += 1 
    self.tweets[userId].append(
      (self.time, tweetId)
    )
  
  def follow(self, followerId, followeeId):
    if followerId != followeeId:
      self.following[followerId].discard(followeeId)
  
  def unfollow(self, followerId, followeeId):
    self.following[followerId].discard(followeeId)
  
  def getNewsFeed(self, userId):
    heap = []
    users = self.following[userId] | {userId}
    for u in users:
      if self.tweets[u]:
        idx = len(self.tweets[u]) - 1 

        time, tweet = self.tweets[u][idx]
        heapq.heappush(
          heap,
          (-time, tweet, u, idx)
        )
    
    ans = []

    while heap and len(ans) < 10:
      _, tweet, user, idx = heapq.heappop(heap)
      ans.append(tweet)
      if idx > 0:
        idx -= 1 
        time, tweet = self.tweets[user][idx]
        heapq.heappush(
          heap, 
          (-time, tweet, user, idx)
        )
    
    return ans

twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))

twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))

twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
