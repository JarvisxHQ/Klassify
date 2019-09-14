import lib.Topic as Topic
import lib.Sentiment as Sentiment
import lib.Insight as Insight
import lib.Summary as Summary

def classifyNews(title, data, getTopic = True, getSentiment = True, getInsight = False, getSummary = True):
    if getTopic:
        topic = Topic.getTopic(title)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(data)
        print("Sentiment: " + str(sentiment))
    if getInsight:
        Insight.getInsight(data)
    if getSummary:
        summary = Summary.getSummary(data)
        print("Summary: " + str(summary))
    return