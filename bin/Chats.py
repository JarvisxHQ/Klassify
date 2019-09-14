import lib.Topic as Topic
import lib.Sentiment as Sentiment
import lib.Insight as Insight
import lib.Urgency as Urgency

def classifyChat(text, getTopic = True, getSentiment = True, getInsight = False, getUrgency = True):
    if getTopic:
        topic = Topic.getTopic(text)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(text)
        print("Sentiment: " + str(sentiment))
    if getInsight:
        Insight.getInsight(text)
    if getUrgency:
        urgency = Urgency.getUrgency(text)
        print("Urgency: " + str(urgency))
    return