import requests
from bs4 import BeautifulSoup


class NewsPage:
    def __init__(self, news_site, url):
        self._queries = news_site['queries']
        self._html = None
        self._visit(url)

    def _select(self, query):
        return self._html.select(query)

    def _visit(self, url):
        response = requests.get(url)
        response.raise_for_status()
        self._html = BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):
    def __init__(self, news_site, url):
        super().__init__(news_site, url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)


class ArticlePage(NewsPage):

    def __init__(self, news_site, url):
        super().__init__(news_site, url)

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else ''

    @property
    def body(self):

        result = self._select(self._queries['article_body'])
        for item in result:

        return result[0].text if len(result) else ''

    @property
    def category(self):
        result = self._select(self._queries['article_category'])
        return result[0].text if len(result) else ''
