bookmark = {
    "name": "my bookmarking",
    "url": "http://this.is/a/bookmarking"
}


def test_get_bookmarks(client):
    assert client.get("/api/v1/bookmarks").status_code == 200


# def test_post_bookmark(client):
#     response = client.post("/api/v1/bookmarks", data=bookmark)
#     assert response.status_code == 201
