import requests
import matplotlib.pyplot as plt
from textblob import TextBlob

def analyze_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else :
        return "Neutral"
    
def news_sentiment():
    topic = input("Enter the topic you want to search about : ")
    #api_key = "pub_fcc108d382a54420ae5035906f87156b"
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={topic}&language=en"
    response = requests.get(url)
    data = response.json()

    headlines = []
    sentiments = []
    creators = []
    for article in data["results"]:
        title = article.get("title")
        creator_get = article.get("creator")
        if title:
            headlines.append(title)
            sentiments.append(analyze_sentiment(title))
            creators.append(creator_get)
    
    positive_count = sentiments.count("Positive")
    negative_count = sentiments.count("Negative")
    neutral_count = sentiments.count("Neutral")

    print("------Sentiment Analysis-------")
    print(f" Positive : {positive_count}")
    print(f"Negative : {negative_count}")
    print(f"Neutral : {neutral_count}")
    for titles,creatorss,sentimentss in zip(headlines,creators,sentiments):
        print(f"Title : {titles}, Author : {creatorss}, Sentiment Analysis = {sentimentss}")
        

    plt.pie(
        [positive_count, negative_count, neutral_count],
        labels= ["positive","negative","neutral"],
        startangle=90,
        )
    plt.title(f"News Sentiment Analysis on Topic : {topic}")
    plt.show()
    
news_sentiment()
 
        


