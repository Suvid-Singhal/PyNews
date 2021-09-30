def News(keywords):
    from requests import get
    import json
    all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[0]+"&apiKey=3cf8688e71e4497d9f9cfd0684457b15").json()
    desired_articles = all_articles.get("articles")
    for i in range(1,len(keywords)):
        all_articles = get("https://newsapi.org/v2/everything?qInTitle="+keywords[i]+"&apiKey=3cf8688e71e4497d9f9cfd0684457b15").json()
        desired_articles += all_articles.get("articles")
    return desired_articles
