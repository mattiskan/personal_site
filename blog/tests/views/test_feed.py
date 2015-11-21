import mongoengine
from pyquery import PyQuery

from blog.views import index

def test_unit_test_index(rf):
    request = rf.get('/')
    response = index(request)
    assert response.status_code == 200


def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code in (200, 302, 303) #  ok or redirect


def test_add_entry(client):
    """Actually requests /blog and counts the number of entries"""
    entry_count_before = _blog_entry_count_in_http_response(client)

    for _ in range(10):
        assert client.get('/blog/create').status_code == 200

    entry_count_after = _blog_entry_count_in_http_response(client)

    assert entry_count_after == (entry_count_before + 10)

    
def _blog_entry_count_in_http_response(client):
    first_response = client.get('/blog/')
    assert first_response.status_code == 200  # extra check

    pq = PyQuery(first_response.content)
    return len(pq('.blog-entry'))


