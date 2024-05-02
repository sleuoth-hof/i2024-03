#!/usr/bin/env python
# coding: utf-8

# In[2]:


import finnhub
import json
from datetime import datetime
import csv
import pandas as pd
import os


# In[3]:


def getfinnhubnews(api_key):
    try:
        finnhub_client = finnhub.Client(api_key=api_key)
        news = list(finnhub_client.general_news('general', min_id=0))
        return news
    except Exception as e:
        print("Fehler beim Abrufen der Nachrichten:", e)
        return []

def convertTimestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def writeNewsToCsv(news, csv_file):
    csv_header = ['category', 'datetime', 'headline', 'id', 'image', 'related', 'source', 'summary', 'url']
    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=csv_header)
            writer.writeheader()
            for entry in news:
                entry['datetime'] = convertTimestamp(entry['datetime'])
                writer.writerow(entry)
        print("Message write in cnv", csv_file)
    except Exception as e:
        print("ERROR", e)


api_key = "cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70"
news = getfinnhubnews(api_key)
if news:
    writeNewsToCsv(news, 'finnhubNews.csv')


# In[80]:


df = pd.read_csv('finnhubNews.csv')
print(df.head(5))


# In[84]:





# In[90]:





# In[ ]:




