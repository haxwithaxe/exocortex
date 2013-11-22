This is the module that pulls and indexes a Twitter feed."""

__authors__ = ["The Doctor <drwho at virtadpt dot net>", "haxwithaxe <me at haxwithaxe dot net>"]

__license__ = "GPLv3"

import json
import twitter
import ..model.bot.Bot

# Classes
class TwitterBot(Bot):
	""" Twwiter scaper Bot. 
		One feed per Bot """

	def __init__(self, feed_id, config_obj):
		""" it give it the global Config object or else it gets the hose again ..."""
		self.conf = config_obj
		self.db = model.twitter.TwitterDB(self.conf.get("twitter-bot", "db-%s" % feed_id))

	def connect(self):
		""" Attempt to connect to Twitter's API server. """
		pass

    def disconnect(self):
        """ disconnect from Twitter"""
        pass

	def init_db(self):
		"""If we had to create the database then we have to load content into it by downloading the whole timeline in chunks and process the information."""
		pass

	def on_start(self):
		# Go into a loop in which we wait for X seconds and download new tweets
		while True:
			self._update()
			# After catching up, send the Indexer a call to update.
			# FIXME: add code to poke indexer
			# Sleep
			time.sleep(self.conf.get_int("twitter-bot", "wait-interval", 3600))
			# Reload the config so config changes can be applied.
			self.conf.reload()
	
	def _update(self):
		""" Download tweets posted since the last recorded tweet in the database. """
		last_tweet = self._get_last_recorded()
		# tweets = download from last_tweet['datestamp-field-name'] to now
		tweets = self._mangle(tweets)
		self._record(tweets)
		pass

	def _mangle(self, tweets):
		""" Format tweets for passing to the database as key value pairs """
		pass

	def _record(self, tweets):
		""" Send tweets to the database"""
		[self.db.set(**tweet) for tweet in tweets]

	def  _get_last_recorded(self):
		""" Get the datestamp of the last tweet added to the database. """
		pass

	def clean(self)
		"""Clean up after ourselves.
			- Delete tempfiles.
		"""
		pass

	def release_db(self):
		"""Close the databases."""
		self.db.close()
