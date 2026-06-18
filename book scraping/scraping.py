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
from bs4 import BeautifulSoup
import pandas as pd

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
    
print(response.text)


soup = BeautifulSoup(response.text,"html.parser")
print(soup.title)



books = soup.find_all("article", class_="product_pod")
print(len(books))

first_book=books[0]
print(first_book.h3.get_text())
rating = first_book.find("p")["class"][1]
print(rating)
print(first_book.find("p", class_="price_color").get_text())
print( first_book.find("p", class_="instock availability").get_text())

titles = []
ratings = []
prices = []
stocks = []
for book in books:
    title=book.h3.get_text()
    rating = book.find("p")["class"][1]
    stock=(book.find("p", class_="instock availability" ).get_text())
    price=(book.find("p", class_="price_color").get_text())
    
    titles.append(title)
    ratings.append(rating)
    prices.append(price)
    stocks.append(stock)
    



#creating dataframe

data=pd.DataFrame({
    "Title":titles,
    "Rating":ratings,
    "Stock":stocks,
    "Price":prices
    })

print(data.head)

print(data.shape)