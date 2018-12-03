import re
import news_page_objects as news
from common import config
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')

def _news_scrapper():
  for n in config()['news_sites']:
    news_site = config()['news_sites'][n]

    host = news_site['url']
    homepage = news.HomePage(news_site, host)

    articles = []
    for link in homepage.article_links:
      article = _fetch_article(news_site, host, link)

      if article:
        print('Article fetched!!!')
        articles.append(article)
        print(article.title)

    print(len(articles))

def _fetch_article(news_site, host, link):
  article = None
  try:
    url = _build_link(host, link)
    print('Start fetching article at {}'.format(url))
    article = news.ArticlePage(news_site, url)
  except (HTTPError, MaxRetryError) as e:
    print('Error while fetching article')

  if article and not article.body:
    print('Invalid Article. There is no body')
    return None

  return article

def _build_link(host, link):
  if is_well_formed_link.match(link):
    return link
  elif is_root_path.match(link):
    return '{}{}'.format(host, link)
  else:
    return '{host}/{uri}'.format(host=host, uri=link)


if __name__ == '__main__':
  _news_scrapper()