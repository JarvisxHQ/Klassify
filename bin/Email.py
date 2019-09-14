import lib.eClassifier as eClassifier
import lib.Urgency as Urgency
import lib.Sentiment as Sentiment

def classifyEmail(email, getTopic = True, getSentiment = True, getUrgency = True):
    if getTopic:
        topic = eClassifier.getEmailTopic(email)
        print(topic)
    if getSentiment:
        sentiment = Sentiment.getSentiment(email)
        print(sentiment)
    if getUrgency:
        urgency = Urgency.getUrgency(email)
        print(urgency)