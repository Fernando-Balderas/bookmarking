from .utils import post_json, put_json, to_json
from .test_folders import test_post_folder

bookmark = {
    "name": "my bookmarking",
    "url": "http://this.is/a/bookmarking"
}


def test_get_bookmarks(client):
    response = client.get("/api/v1/bookmarks")
    data = to_json(response.data)
    bookmarks = data.get("data")
    assert response.status_code == 200
    assert bookmarks != None
    return bookmarks


def test_post_bookmark(client):
    response = post_json(client, "/api/v1/bookmarks", bookmark)
    data = to_json(response.data)
    new_bookmark = data.get("data")
    assert response.status_code == 201
    assert data.get("message") == "Bookmark created"
    assert new_bookmark.get("id") != None
    assert new_bookmark.get("name") != None
    assert new_bookmark.get("url") != None
    assert ("folder_id" in new_bookmark) == True
    assert new_bookmark.get("created_at") != None
    assert new_bookmark.get("updated_at") != None
    return new_bookmark


def test_get_folderbookmark(client):
    new_folder = test_post_folder(client)
    folder_id = str(new_folder.get("id"))
    response = client.get("/api/v1/bookmarks/folders/" + folder_id)
    data = to_json(response.data)
    assert response.status_code == 200
    assert data.get("data") != None


def test_put_bookmark(client):
    new_bookmark = test_post_bookmark(client)
    bookmark_id = str(new_bookmark.get("id"))
    update = {
        "name": "edited bookmarking",
        "url": "http://this.is/my/edited/bookmarking"
    }
    response = put_json(client, "/api/v1/bookmarks/" + bookmark_id, update)
    data = to_json(response.data)
    assert response.status_code == 200
    assert data.get("data") == bookmark_id


def test_delete_bookmark(client):
    new_bookmark = test_post_bookmark(client)
    bookmark_id = str(new_bookmark.get("id"))
    response = client.delete("/api/v1/bookmarks/" + bookmark_id)
    data = to_json(response.data)
    assert response.status_code == 200
    assert data.get("data") == bookmark_id
