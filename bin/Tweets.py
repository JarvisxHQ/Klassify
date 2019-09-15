import lib.Topic as Topic
import lib.Sentiment as Sentiment

def classifyTweet(tweet, getTopic = True, getSentiment = True):
    topic = ""
    sentiment = ""
    if getTopic:
        topic = Topic.getTopic(tweet)
        topic = "Topic: " + str(topic)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(tweet)
        sentiment = "Sentiment: " + str(sentiment)
        print("Sentiment: " + str(sentiment))
    return topic, sentiment