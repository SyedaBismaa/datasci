# -*- coding: utf-8 -*-
"""
Indeed Scraper - Save HTML
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Open Chrome
driver = webdriver.Chrome()

# Open Indeed
driver.get("https://in.indeed.com/jobs?q=data+scientist")

# Wait for page to load
time.sleep(5)

# Get HTML
html = driver.page_source

# Save HTML file
with open("indeed.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML Saved Successfully!")

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Quick test
titles = []

for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)

    if text:
        titles.append(text)

# Create DataFrame
df = pd.DataFrame(titles, columns=["Job Title"])

print("\nFirst Titles Found:")
print(df.head())

print("\nTotal Titles Found:", len(df))

# Save CSV
df.to_csv("indeed_jobs.csv", index=False)

print("✅ CSV Saved Successfully!")

# Show files in current folder
print("\nCurrent Working Directory:")
print(os.getcwd())

print("\nFiles in Folder:")
print(os.listdir())

# Close browser
driver.quit()