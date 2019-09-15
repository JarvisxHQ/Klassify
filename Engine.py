import bin.News as News
import bin.Article as Article
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

eel.start('index.html', size=(1000,600))