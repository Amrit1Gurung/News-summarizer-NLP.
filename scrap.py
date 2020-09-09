import re
from bs4 import BeautifulSoup
import requests

#webpage url
URL = "https://kathmandupost.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

sidebar_menu = soup.find_all('div', class_ = "offcanvas")
sidebar = sidebar_menu[0]
menu_list = sidebar.find_all('a', class_ = "menu-item")

news_categories = []
news_categories_links = []
for list in menu_list:
  category = list.string
  url = list['href']
  news_categories_links.append("https://kathmandupost.com" + url)
  news_categories.append(category)

news_categores_and_links = dict(zip(news_categories,news_categories_links))

del news_categores_and_links['Wheels']
del news_categores_and_links['Visual Stories']
del news_categores_and_links['Weekender']
del news_categores_and_links['Interviews']
del news_categores_and_links['Culture & Arts']
del news_categores_and_links['Travel']
del news_categores_and_links['Investigations']
del news_categores_and_links['Climate & Environment']


Title = []
Date = []
Articles = []
NewsCategory = []
newsLink = []
for category,link in news_categores_and_links.items():
  newscategory = category
  url = link
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')

  container_block = soup.find_all('div', class_ = "block--morenews")
  first_block = container_block[0]
  article_link = first_block.find_all('article', class_ = "article-image")

  links = []

  for list in article_link:
    sss = list.find_all('figure')
    for s in sss:
      xx = s.find('a')
      linkarticle = xx['href']
      links.append("https://kathmandupost.com" + linkarticle)


  # collecting data like author name , title and articles 
  title = []
  date_list =[]
  thearticle = []
  news_Category = []
  #newsLink = []
  for pagelink in links:
    ##
    # store the text for each article
    paragraphtext = []    
    # get url
    url = pagelink
    # get page text
    page = requests.get(url)
    #  parse with BFS
    soup = BeautifulSoup(page.text, 'html.parser')
    published_date = soup.find('div', class_="updated-time").text
    date = published_date[15:].strip()
    date_list.append(date)

    art_container = soup.find('div', class_ = "col-sm-8")
    #art_container = art_container[0]
    art_title =  art_container.find('h1')
    thetitle = art_title.get_text() 

    # get main article page
    articlebody = soup.find_all('div', class_="subscribe--wrapperx")[0]  # encloses main article body
    # get text
    articletext = articlebody.find_all('p')    # list of <p> tags and its contents
    # print text
    for paragraph in articletext[:-1]:
      ##
      # get the text only
      text = paragraph.get_text()
      paragraphtext.append(text)
    #
    # combine all the paragraphs into a article
    thearticle.append(paragraphtext)
    title.append(thetitle)
    news_Category.append(category)
  myarticle = [' '.join(article) for article in thearticle]
  Date.append(date_list)
  Title.append(title)
  NewsCategory.append(news_Category)
  Articles.append(myarticle)
  newsLink.append(links)

news_title = [j for i in Title for j in i]
news_date = [j for i in Date for j in i]
news_cat = [j for i in NewsCategory for j in i]
newsarticle = [j for i in Articles for j in i]
newsLINKS = [j for i in newsLink for j in i]


# create dataframe of collected dataimport pandas as pd
import pandas as pd

news_articles = pd.DataFrame()
news_articles['Title'] = news_title
news_articles['date'] = news_date
news_articles['Article'] = newsarticle
news_articles['Category'] = news_cat
news_articles['PageLinks'] = newsLINKS

news_articles.to_csv('news_articles.csv')
  