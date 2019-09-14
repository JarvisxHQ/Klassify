import lib.Topic as Topic
import lib.Sentiment as Sentiment

def classifyTweet(tweet, getTopic = True, getSentiment = True):
    if getTopic:
        topic = Topic.getTopic(tweet)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(tweet)
        print("Sentiment: " + str(sentiment))
    return