
import tweepy


CONSUMER_API_KEY = ""
CONSUMER_API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

twitter.update_status("test!") 


'''
query_result = twitter.friends()

with open("twitterfriends.txt", "w") as text_file:
    for tweet in query_result:
        text_file.write(str(tweet))
'''