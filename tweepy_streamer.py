from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API

%load 'twitter_credentials.py' #file that contains credentials as shown below

# ACCESS_TOKEN = ""
# ACCESS_TOKEN_SECRET = ""
# CONSUMER_KEY = ""
# CONSUMER_SECRET = ""

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['keto','ketodiet','whole30','whole30diet','glutenfree','glutenfreediet','mediterraneandiet','lowfat', 'lowfatdiet','paleo','paleodiet','celeryjuice'])
