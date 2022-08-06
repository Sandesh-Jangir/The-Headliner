import eel
import requests
import json
from api_key import key
eel.init("web")
@eel.expose
def bbc_data():
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={key}"
    news = requests.get(url).text
    news_py = json.loads(news)
    articles = news_py['articles']
    return articles

eel.start("Headlines.html")