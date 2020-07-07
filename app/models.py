class NewsSource:
    '''
    class that creates instance of NewsSource
    '''
    def __init__(self,id,name):
        '''
        function to create the NewsSource instance
        '''
        self.id = id
        self.name = name
        
class Article:
    '''
    Class that creates instance of an Article
    '''
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
        '''
        function that creates initial blueprint of Article
        '''
        self.id = id
        self.author = author 
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt