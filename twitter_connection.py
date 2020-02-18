import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet(tweet):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "someKey",
    "consumer_secret"     : "someSecret",
    "access_token"        : "someToken",
    "access_token_secret" : "someAccessToken"
    }

  api = get_api(cfg)
  status = api.update_status(status=tweet)


