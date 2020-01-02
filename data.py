def News():
    from datetime import date, timedelta
    from requests import get
    import json
    today = date.today()
    tendaysago = today - timedelta(days=5)

    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Open-Source&apiKey=3cf8688e71e4497d9f9cfd0684457b15").json()
    desired_articles = all_articles.get("articles")
    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Linux&apiKey=3cf8688e71e4497d9f9cfd0684457b15").json()
    desired_articles += all_articles.get("articles")
    all_articles = get("https://newsapi.org/v2/everything?qInTitle=Android&apiKey=3cf8688e71e4497d9f9cfd0684457b15").json()
    desired_articles += all_articles.get("articles")
    return desired_articles
