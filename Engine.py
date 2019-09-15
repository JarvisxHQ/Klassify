import bin.News as News
import bin.Article as Article
import bin.Tweets as Tweet
import bin.Email as Email
import bin.Chats as Chats
import eel
eel.init('web')

@eel.expose
def classifyNewsArticle(title, article):
    title = ["" + str(title)]
    article = ["" + str(article)]
    topic, sentiment, summary = News.classifyNews(title, article)
    eel.consolePrint(topic, sentiment, summary)

@eel.expose
def classifyArticle(title, article):
    title = ["" + str(title)]
    article = ["" + str(article)]
    topic, sentiment, summary = Article.classifyArticle(title, article)
    eel.consolePrint(topic, sentiment, summary)

@eel.expose
def classifyTweet(tweet):
    tweet = ["" + str(tweet)]
    topic, sentiment = Tweet.classifyTweet(tweet)
    eel.consolePrint(topic, sentiment)


@eel.expose
def classifyEmail(email):
    email = ["" + str(email)]
    topic, sentiment, urgency = Email.classifyEmail(email)
    eel.consolePrint(topic, sentiment, urgency)

@eel.expose
def classifyChats(chat):
    chat = ["" + str(chat)]
    topic, sentiment, urgency = Chats.classifyChat(chat)
    eel.consolePrint(topic, sentiment, urgency)

eel.start('index.html', size=(1000,600))