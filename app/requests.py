import urllib.request,json
from .models import NewsSource,Article

api_key = None
sources_base_url = None
source_articles_base_url = None

def configure_request(app):
    '''
    function to get api_key and base_url values
    '''
    global api_key,sources_base_url,source_articles_base_url
    api_key = app.config['NEWS_API_KEY']
    sources_base_url = app.config['NEWS_SOURCES_API_BASE_URL']
    source_articles_base_url = app.config['NEWS_SOURCE_ARTICLES_BASE_URL']

def get_sources(category):
    '''
    function to get news sources
    '''
    get_sources_url = 'http://newsapi.org/v2/sources?category={}&apiKey=7f82d84e45d64550bacc0dd3433aae1a'.format(category)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_lists = get_sources_response['sources']
            sources_results = process_results(sources_results_lists)

        return sources_results

def process_results(sources_list):
    '''
    function that takes response list and transforms it to a list of objects
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')

        source_object = NewsSource(id,name)
        sources_results.append(source_object)

    return sources_results

def get_source_articles(source):
    '''
    function that returns the articles of selected news source
    '''
    get_source_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=7f82d84e45d64550bacc0dd3433aae1a'.format(source)

    with urllib.request.urlopen(get_source_articles_url) as url:
        get_source_articles_data = url.read()
        source_articles_response = json.loads(get_source_articles_data)

        articles_result = None

        if source_articles_response['articles']:
            source_articles_list = source_articles_response['articles']
            articles_result = process_articles(source_articles_list)

        return articles_result

def process_articles(articles_list):
    '''
    function that takes article lists formats to objects
    '''
    articles_results = []

    for article in articles_list:
        id = article.get('source.id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        imageUrl = article.get('urlToImage')
        published = article.get('publishedAt')

        article_object = Article(id,author,title,description,url,imageUrl,published)
        articles_results.append(article_object)

    return articles_results         

def get_article(id):

    get_article_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=7f82d84e45d64550bacc0dd3433aae1a'.format(id)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None

        if article_details_response:
            id = article_details_response.get('source.id')
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            imageUrl = article_details_response.get('urlToImage')
            published = article_details_response.get('publishedAt')
    
            article_object = Article(id,author,title,description,url,imageUrl,published)

        return article_object

        
def search_sources(source_name):
    '''
    function that searches for news sources based on name of the source
    '''
    search_source_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(source_name,api_key)
    with urllib.request.urlopen(search_source_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)

        search_sources_results = None

        if search_sources_response['articles']:
            search_sources_list = search_sources_response['articles']
            search_sources_results = process_results(search_sources_list)

        return search_sources_results