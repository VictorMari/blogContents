import requests
import pymongo
from dataclasses import dataclass



@dataclass
class Blog:
    url: str
    content: str
    media: str
    extractedDate: str

    



class BlogCrawler:
    def __init__(self, urls):
        self.urls = urls

    def blogs(self, url):
        for url in self.urls:
            yield self._get_blog(url)

    def _get_blog(self, url):
        # get blog html using requests
        # save extracted blog html
        # extract blog data
        # return blog class
        pass

class URLExtractor:
    def __init__(self):
        self.mediumUrl = "medium.com"

    def get_medium_tech_blog_urls(self):
        pass

class BlogStorage:
    def __init__(self):
        pass
    
    def save_extracted(self, blog):
        pass

    def persist_blogs(self, blog):
        pass


if __name__ == "__main__":
    extractor_instance = URLExtractor()    