import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url = "https://www.rottentomatoes.com/m/him_2025_2/reviews"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

review_containers = soup.find_all("div", class_="review-text-container")

analyzer = SentimentIntensityAnalyzer()

positive = 0
negative = 0
neutral = 0


for container in review_containers:
    review_text = container.find("p", class_="review-text").get_text(strip=True)
    
    scores = analyzer.polarity_scores(review_text)
    compound = scores['compound']
    
    if compound >= 0.05:
        sentiment = "Positive"
        positive += 1
    elif compound <= -0.05:
        sentiment = "Negative"
        negative+=1
    else:
        sentiment = "Neutral"
        neutral+=1
    
    print("Review:", review_text)
    print("Sentiment:", sentiment)
    print("Scores:", scores)
    print("-"*50)
    

print("Summary:")
print(f"Positive reviews: {positive}")
print(f"Negative reviews: {negative}")
print(f"Neutral reviews: {neutral}")    
            
total = positive + negative + neutral
if positive/total >= 0.6:
    print("       recommended 🤍")
elif negative/total >= 0.5:
    print("     don't recommend ❌")
else:
    print("      mixed reviews ⚖️")    