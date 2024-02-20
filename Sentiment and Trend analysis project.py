#!/usr/bin/env python
# coding: utf-8

# ### Sentiment Analysis of Amazon's Sales 

# In[20]:


import pandas as pd
import textblob
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\HP\Desktop\vishnu\Amazon sales data.csv")
#df
#print(df['review_title'][0])
t = df['review_title'][0]

def find_sentiment(t):
    try:
        analyse = textblob.TextBlob(t)
        if analyse.sentiment.polarity < 0:
            return "Negative"
        elif analyse.sentiment.polarity > 0:
            return "Positive"
        else:
            return "Neutral"
    except:
        return "Neutral"
#find_sentiment()
# creating new column for sentiment result
df["sentiment_result"] = df["review_title"].apply(lambda row : find_sentiment(row))
# for counting sentiment column
result = {}
for senti,grp in df.groupby("sentiment_result"):
    print(senti,len(grp))
    result[senti] = len(grp)
print(result)
x = list(result.keys())
y = list(result.values())
plt.bar(x,y,color = "hotpink")
plt.scatter(x,y,color = 'm',marker = 'D')
plt.plot(x,y,color = 'c',ls = '-.',linewidth = '3')
plt.show()


# ### Trend Analysis of Amason's Sales 

# In[21]:


def find_sentiment(t):
    try:
        analyse = textblob.TextBlob(t)
        if analyse.sentiment.polarity < 0:
            return -1
        elif analyse.sentiment.polarity > 0:
            return 1
        else:
            return 0
    except:
        return 0
x = list(range(1,len(df)+1))
y = []
As_senti = 0
for i in x:
    t = df['review_title'][i-1]
    As_senti += find_sentiment(t)
    y.append(As_senti)
plt.plot(x,y,color="c")
plt.show()    

