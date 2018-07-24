import tweepy
from textgenrnn import textgenrnn
import io
from contextlib import redirect_stdout

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

buf = io.StringIO()
with redirect_stdout(buf):
	textgen.generate(1, temperature=.69, max_gen_length=140)

textgen = textgenrnn(weights_path='realDonaldTrump_twitter_weights.hdf5')
tweet = buf.getvalue()
if tweet.rfind(".") != -1:
	tweet = tweet[:tweet.rfind(".") + 1]
api.update_status(status = tweet)