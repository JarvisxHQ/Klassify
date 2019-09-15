import lib.Topic as Topic
import lib.Sentiment as Sentiment
import lib.Insight as Insight
import lib.Summary as Summary

def classifyNews(title, data, getTopic = True, getSentiment = True, getInsight = False, getSummary = True):
    topic = ""
    sentiment = ""
    summary = ""
    if getTopic:
        topic = Topic.getTopic(title)
        topic = "Topic: " + str(topic)
        print("Topic: " + str(topic))
    if getSentiment:
        sentiment = Sentiment.getSentiment(data)
        sentiment = "Sentiment: " + str(sentiment)
        print("Sentiment: " + str(sentiment))
    if getInsight:
        Insight.getInsight(data)
    if getSummary:
        summary = Summary.getSummary(data)
        summary = "Summary: " + str(summary)
        print("Summary: " + str(summary))
    return topic, sentiment, summary