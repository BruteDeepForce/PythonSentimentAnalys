from googleapiclient.discovery import build
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):                     ##Standart sentiment analys function
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    sentiment_res = sentiment_scores['compound']
    
    plt.bar(sentiment_scores.keys(), sentiment_scores.values())    #i have use plt.bar. because i want to see Bar design

    plt.title("Gelen Yorum:\n"+ text)
    plt.xlabel('DUYGUSAL DURUM')
    plt.ylabel('DEĞER')
    plt.show()     
    input("Please Enter to Exit...") 
    
    if sentiment_res >= 0.3:                            
        return 'positive'
    elif sentiment_res <= -0.3:
        return 'negative'
    else:
        return 'neutral'
    
    
api_key = "Your Api Key"             ## https://console.cloud.google.com  youtube data api v3.

youtube = build('youtube', 'v3', developerKey=api_key)          

video_id = "Yotube Video-id"                                       

response = youtube.commentThreads().list(                       
    part='snippet',
    videoId=video_id,
    textFormat='plainText'
).execute()

for item in response['items']:                                                  
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    sentiment = analyze_sentiment(comment)
    print(f"Comment: {comment}\nSentiment: {sentiment}\n")
    




 
