def News(keywords):
    from requests import get
    import json
    all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[0]+"&apiKey=<YOUR-KEY-HERE>").json()
    desired_articles = all_articles.get("articles")
    for i in range(1,len(keywords)):
        all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[i]+"&apiKey=<YOUR-KEY-HERE>").json()
        desired_articles += all_articles.get("articles")
    return desired_articles
