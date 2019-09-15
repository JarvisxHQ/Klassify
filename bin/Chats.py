import lib.Topic as Topic
import lib.Sentiment as Sentiment
import lib.Insight as Insight
import lib.Urgency as Urgency

def classifyChat(text, getTopic = True, getSentiment = True, getInsight = False, getUrgency = True):
    topic = ""
    sentiment = ""
    urgency = ""
    if getTopic:
        topic = Topic.getTopic(text)
        topic = "Topic: " + str(topic)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(text)
        sentiment = "Sentiment: " + str(sentiment)
        print("Sentiment: " + str(sentiment))
    if getInsight:
        Insight.getInsight(text)
    if getUrgency:
        urgency = Urgency.getUrgency(text)
        urgency = "Urgency: " + str(urgency)
        print("Urgency: " + str(urgency))
    return topic, sentiment, urgency