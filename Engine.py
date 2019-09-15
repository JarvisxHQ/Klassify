import bin.News as News
import eel
eel.init('web')

@eel.expose
def classifyNewsArticle(title, article):
    title = ["" + str(title)]
    article = ["" + str(article)]
    News.classifyNews(title, article)


eel.start('index.html', size=(1000,600))