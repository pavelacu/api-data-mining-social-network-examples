import tweepy
import yaml

with open("../config-tweepy.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)

consumer_key = cfg['consumer_key']
consumer_secret = cfg['consumer_secret']
access_token = cfg['access_token']
access_secret = cfg['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Autenticacion en la plataforma
api = tweepy.API(auth)
# Muestra nuestro TimeLine
#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    print(status.text)

#for tweet in tweepy.Cursor(api.search,q="google",rpp=100,result_type="recent", include_entities=True,lang="en").items():
#for tweet in tweepy.Cursor(api.user_timeline, id="AlexElRojo", ).items(10):
#for tweet in tweepy.Cursor(api.search,q="from:amilcarmontejo ROBADA", rpp=100, result_type="mixed", until="2018-05-18",include_entities=True,lang="en").items(100):
for tweet in tweepy.Cursor(api.search,q="from:amilcarmontejo ROBADA", rpp=100, result_type="mixed", until="2018-05-18",include_entities=True).items(100):
    print(tweet.created_at, tweet.text)
