

import requests
from bs4 import BeautifulSoup


class HttpQuery:

    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.req = requests.get(url=self.url, params=self.params)

    def get_page_html(self):
        """ """

        if self.req.status_code == 200:
            return self.req.text
        else:
            print('Server status code: ', self.req.status_code)
            return

class ElementPage:

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'lxml')

class ElementPageParent(ElementPage):
    
    def get_parent_element(self):
        """ """
        abc = self.soup.find('div', class_='')

class ElementPageChild(ElementPage):
 
    def get_child_element(self):
        """ """
        abc = self.soup.find('div', class_='')

class ElementPageGrandchild(ElementPage):

    def get_grandchild_element(self):
        """ """ 
        abc = self.soup.find('div', class_='')



