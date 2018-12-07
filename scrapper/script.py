from db import db
from urllib3.exceptions import MaxRetryError
from requests.exceptions import HTTPError
from common import config
from utils import build_link
import news_page_objects as news
import datetime


def _news_scrapper():
    for n in config()['news_sites']:
        news_site = config()['news_sites'][n]

        host = news_site['url']
        homepage = news.HomePage(news_site, host)

        for link in homepage.article_links:
            article = _fetch_article(news_site, host, link)

            if article:
                # articles.append(article)
                db.news.insert_one({
                    "title": article.title,
                    "content": article.body,
                    "category": article.category,
                    "image": build_link(host, article.image),
                    "date": datetime.datetime.utcnow()
                })


def _fetch_article(news_site, host, link):
    article = None
    try:
        url = build_link(host, link)
        print('Start fetching article at {}'.format(url))
        article = news.ArticlePage(news_site, url)
    except (HTTPError, MaxRetryError):
        print('Error while fetching article')

    if article and not article.body:
        print('Invalid Article. There is no body')
        return None

    return article


if __name__ == '__main__':
    _news_scrapper()
