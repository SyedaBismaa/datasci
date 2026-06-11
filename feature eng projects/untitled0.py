# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:42:03 2026

@author: syeda
"""

#requests.get()
#BeautifulSoup()
#find()
#find_all()
#select()


import requests
import bs4 as BeautifulSoup
import pandas

url = "https://books.toscrape.com/?utm_source=chatgpt.com"

response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

books=soup.find_all("article",class_="product_pod")


for book in books[:5]:
    title=book.h3.a["title"]
    price=book.find("p",class_="price_color").text
    rating= book.find("p",class_="star-rating")["class"][1]
    
    print(title)
    print(price)
    print(rating)
    print("-"*30)
    