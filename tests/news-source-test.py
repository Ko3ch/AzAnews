import unittest
from app.models import NewsSource

NewsSource = NewsSource

class TestNewsSource(unittest.TestCase):
    '''
    Class to create test cases for NewSource
    '''
    def setup(self):
        '''
        function to initialize NewsSource 
        '''
        self.new_newsSource = NewsSource("bbc-news","BBC News")
    
    def test_instance(self):
         self.assertTrue(isinstance(self.new_newsSource,NewsSource))