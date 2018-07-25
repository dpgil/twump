import tweepy
import io
import os
from textgenrnn import textgenrnn
from contextlib import redirect_stdout

# Constants
MAX_TWEET_LENGTH = 140

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)
while True:
	buf = io.StringIO()
	textgen = textgenrnn(weights_path='tweet-generator/realDonaldTrump_twitter_weights.hdf5')
	with redirect_stdout(buf):
		textgen.generate(1, temperature=.69, max_gen_length=MAX_TWEET_LENGTH)

	tweet = buf.getvalue()
	# Trim to last sentence.
	if tweet.rfind('.') != -1:
		tweet = tweet[:tweet.rfind('.') + 1]
	# Trim last word if we are at max tweet size
	# so we don't post broken words.
	if len(tweet) == MAX_TWEET_LENGTH:
		tweet = tweet[:tweet.rfind(' ')]
	# Post the tweet so long as it's not all periods.
	if tweet != len(tweet) * tweet[0]:
		api.update_status(status = tweet)
		break