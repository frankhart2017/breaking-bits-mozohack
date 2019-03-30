import tweepy
import re

consumer_key = "hWLYACc1Taa147sr5mfhWnJrg"
consumer_secret = "bynK7xQonzySkp8Ee0aQGH33J15Z76VEirQhnEVubTQYZhmK8V"
access_key = "3793515253-LjJuxTBzbAslERcynp9jbp0nXiO9F74bmeq86pK"
access_secret = "65hqEtpgvzysIAASQ3Z6rKu1c1An7IH56g48tVoHrLmhx"

# Function to extract tweets
def get_tweets(username):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    tweets = api.mentions_timeline()
    tweets_mine = api.user_timeline()

    tmp = []
    tmp_screen_names = []
    tmp_mine = []

    tweets_for_csv = [tweet.text for tweet in tweets]
    tweets_mine_for_csv = [tweet_mine.text for tweet_mine in tweets_mine]

    for j in tweets_for_csv:
        j = re.sub(r"(?:\@|https?\://)\S+", "", j)
        tmp.append(j.strip())

    for tweet in tweets:
        tmp_screen_names.append(tweet.user.screen_name)

    for j in tweets_mine_for_csv:
        j = re.sub(r"(?:\@|https?\://)\S+", "", j)
        tmp_mine.append(j.strip())

    return tmp, tmp_screen_names, tmp_mine
