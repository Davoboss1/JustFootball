import requests,re
from bs4 import BeautifulSoup
from datetime import date
from news.models import football_posts
class news:
    def __init__(self,title,summary,date,news,image):
        self.title = title
        self.summary = summary
        self.date = date
        self.news = news
        self.image = image
    def __str__(self):
        return f"{self.date}: {self.title}"

fetched_news = []
def from_skysports(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    title = soup.find("span",class_="article__long-title").text
    summary = soup.find("p",itemprop="description").text
    date = soup.find("p",class_="article__header-date-time").text
    image = soup.find("img",class_="widge-figure__image auto-size__target")["src"]
    news_data = ""
    news_list = soup.find_all("p")
    for n in news_list:
        if not n.attrs:
            news_data += n.text + "\n\n"
    news_data += "\n Source (Skysports)"
    return news(title,summary,date,news_data,image)

def skysports_data():
    skysportspage = requests.get("https://www.skysports.com/football/news/")
    soup = BeautifulSoup(skysportspage.content,"html.parser")
    links = soup.find_all("a",class_="news-list__headline-link")
    for link in links:
        try:
        	n = from_skysports(link["href"])
        	fetched_news.append(n)
        	print(f"{n.title} added to list.")
        except:
            pass

#Bbc sports
def from_bbc_sports(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    title = soup.find("h1",class_="story-headline gel-trafalgar-bold").text
    summary = soup.find("p",class_="sp-story-body__introduction").text
    date = soup.find("abbr",class_="abbr-on medium-abbr-off")["title"]
    image = soup.select("img[sizes]")[0]
    image = image["src"]
    news_data = ""
    news_list = soup.find_all("p")
    inc = 0
    for n in news_list:
        if not n.attrs:
        	if inc == 0:
        		del news_list[len(news_list)-1]
        	else:
        		text = n.text + "\n\n"
        		print(text)
        		news_data += text
        	inc +=1
    news_data += "\n Source (Bbc sports)"

    return news(title,summary,date,news_data,image)

def bbc_data():
    req = requests.get("https://www.bbc.com/sport/football/")
    soup = BeautifulSoup(req.content,"html.parser")
    links = soup.find_all("a",class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-pica-bold")
    for link in links:
        l = link["href"]
        if re.match("^/sport/football/",l):
            try:
                n = from_bbc_sports("https://www.bbc.com"+l)
                fetched_news.append(n)
                print(f"{n.title} added to list.")
            except:
                print("Failed")
                
def run():
    skysports_data()
    bbc_data()
    print("completed.")
    print(fetched_news)
    for data in fetched_news:
    	if football_posts.objects.filter(Title=data.title,summary=data.summary).exists():
    		print("Exists")    	
    	else:
    		football_posts.objects.create(Title=data.title,images=data.image,summary=data.summary,news=data.news)
    		print("Adding to database")

