

from obj_parser.pages import HttpQuery, ElementPageParent, ElementPageChild, ElementPageGrandchild



def test_query():
    """ """
    query = HttpQuery(url, params=None)
    html = query.get_page_html()
    return html

def element_parent_page(html):
    """ """
    elements = ElementPageParent(html)
    data_page = elements.get_parent_page()
    print(data_page)

if __name__ == '__main__':
    
    url = ""

    html = test_query()
    element_parent_page(html)

