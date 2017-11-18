import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweet(tweet):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "oyA4zCfF5gib2gpbeFI2fRkck",
    "consumer_secret"     : "0eLW5cXg4AUocbYHyKr6K2DTwHcWIahKzqIfIiaKmbCC7hFx3A",
    "access_token"        : "912818063543869441-v2E1YzoYCSm7xTZHPbtQkJr92TNevAf",
    "access_token_secret" : "eI3HtXu7HRHsjOWiGAzPqLmvKMrajQnjhMVDoBFxjNbMT"
    }

  api = get_api(cfg)
  status = api.update_status(status=tweet)


