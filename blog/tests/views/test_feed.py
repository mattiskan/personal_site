from pyquery import PyQuery

from blog.views import index


def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code in (200, 302, 303) #  ok or redirect

