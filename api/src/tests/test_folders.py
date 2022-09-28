from .utils import post_json, put_json, to_json

folder = {
    "name": "shared",
    "description": "shared folder with friends"
}


def test_get_folders(client):
    response = client.get("/api/v1/folders")
    data = to_json(response.data)
    folders = data.get("data")
    assert response.status_code == 200
    assert folders != None
    return folders


def test_post_folder(client):
    response = post_json(client, "/api/v1/folders", folder)
    data = to_json(response.data)
    new_folder = data.get("data")
    assert response.status_code == 201
    assert data.get("message") == "Folder created"
    assert new_folder.get("id") != None
    assert new_folder.get("name") != None
    assert new_folder.get("description") != None
    assert new_folder.get("created_at") != None
    assert new_folder.get("updated_at") != None
    return new_folder


def test_put_folder(client):
    new_folder = test_post_folder(client)
    folder_id = str(new_folder.get("id"))
    update = {
        "name": "Shared friends",
        "description": "This folder is for shared bookmarks with friends"
    }
    response = put_json(client, "/api/v1/folders/" + folder_id, update)
    data = to_json(response.data)
    assert response.status_code == 200
    assert data.get("data") == folder_id


def test_delete_folder(client):
    new_folder = test_post_folder(client)
    folder_id = str(new_folder.get("id"))
    response = client.delete("/api/v1/folders/" + folder_id)
    data = to_json(response.data)
    assert response.status_code == 200
    assert data.get("data") == folder_id
