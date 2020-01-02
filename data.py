def News():
    from datetime import date, timedelta
    from requests import get
    import json
    today = date.today()
    tendaysago = today - timedelta(days=5)

    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Open-Source&apiKey=<YOUR-API-KEY-HERE>").json()
    desired_articles = all_articles.get("articles")
    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Linux&apiKey=<YOUR-API-KEY-HERE>").json()
    desired_articles += all_articles.get("articles")
    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Android&apiKey=<YOUR-API-KEY-HERE>").json()
    desired_articles += all_articles.get("articles")
    return desired_articles
