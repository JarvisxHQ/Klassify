import lib.eClassifier as eClassifier
import lib.Urgency as Urgency
import lib.Sentiment as Sentiment

def classifyEmail(email, getTopic = True, getSentiment = True, getUrgency = True):
    topic = ""
    sentiment = ""
    urgency = ""
    if getTopic:
        topic = eClassifier.getEmailTopic(email)
        topic = "Topic: " + str(topic)
        print(topic)
    if getSentiment:
        sentiment = Sentiment.getSentiment(email)
        sentiment = "Sentiment: " + str(sentiment)
        print(sentiment)
    if getUrgency:
        urgency = Urgency.getUrgency(email)
        urgency = "Urgency: " + str(urgency)
        print(urgency)
    return topic, sentiment, urgency