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
    News.classifyNews(title, article)

@eel.expose
def classifyArticle(title, article):
    title = ["" + str(title)]
    article = ["" + str(article)]
    Article.classifyArticle(title, article)

@eel.expose
def classifyTweet(tweet):
    tweet = ["" + str(tweet)]
    Tweet.classifyTweet(tweet)

@eel.expose
def classifyEmail(email):
    email = ["" + str(email)]
    Email.classifyEmail(email)

@eel.expose
def classifyChats(chat):
    chat = ["" + str(chat)]
    Chats.classifyChat(chat)

eel.start('index.html', size=(1000,600))