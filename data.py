import os
api_key=os.getenv('key')
def News(keywords):
    from requests import get
    import json
    all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[0]+"&apiKey="+api_key).json()
    desired_articles = all_articles.get("articles")
    for i in range(1,len(keywords)):
        all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[i]+"&apiKey="+api_key).json()
        desired_articles += all_articles.get("articles")
    return desired_articles
