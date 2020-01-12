from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import configurations
import re
from dateutil.parser import parse

@api_view(['GET'])
def get_tweet_by_hashtag(request,hashtag):

	hashtag = "#"+hashtag.lower()+ " -filter:retweets"

	limit = request.query_params.get('limit',30)
	tweets = configurations.tweepy.Cursor(configurations.api.search,
		q=hashtag,
		lang="en",
		).items(int(limit))

	output = []
	accounts = {"account":""}
	for tweet in tweets:
		temp = {"fullname":"","href":"","id":0,"hashtags":[],"date":"","likes":0,"replies":0,"retweets":0,"text":""}
		
		temp["fullname"] = tweet.user.name
		temp["href"] = "/"+tweet.user.screen_name
		temp["id"] = tweet.user.id

		dt = parse(str(tweet.created_at))

		temp["date"] = str(dt.time().strftime("%I:%M %p")) +" - "+str(dt.date().strftime("%d %b %Y"))

		temp["likes"] = tweet.favorite_count
		temp["retweets"] = tweet.retweet_count
		plain_text = tweet.text
		temp["text"] = plain_text
		hashtagList = []
		split = re.split('(\W)', plain_text)

		for i in range(0,len(split)):
	
		    if split[i] == "#":
		        hashtagList.append("#"+split[i+1])
		hashtagList  
		temp["hashtags"] = hashtagList
 
		output.append(temp)

	accounts["account"]=output
	return Response(accounts)



@api_view(['GET'])
def get_user_tweets(request,account_name):

	account_name = "@"+account_name
	limit = request.query_params.get('limit',30)
	tweets = configurations.api.user_timeline(account_name,count=int(limit))
	output = []
	accounts = {"account":""}
	for tweet in tweets:
		temp = {"fullname":"","href":"","id":0,"hashtags":[],"date":"","likes":0,"replies":0,"retweets":0,"text":""}
		
		temp["fullname"] = tweet.user.name
		temp["href"] = "/"+tweet.user.screen_name
		temp["id"] = tweet.user.id

		dt = parse(str(tweet.created_at))

		temp["date"] = str(dt.time().strftime("%I:%M %p")) +" - "+str(dt.date().strftime("%d %b %Y"))

		temp["likes"] = tweet.favorite_count
		temp["retweets"] = tweet.retweet_count
		plain_text = tweet.text
		temp["text"] = plain_text
		hashtagList = []
		split = re.split('(\W)', plain_text)

		for i in range(0,len(split)):
	
		    if split[i] == "#":
		        hashtagList.append("#"+split[i+1])
		hashtagList  
		temp["hashtags"] = hashtagList
 
		output.append(temp)

	accounts["account"]=output
	return Response(accounts)








