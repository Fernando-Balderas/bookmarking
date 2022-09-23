folder = {
    "name": "shared",
    "description": "shared folder with friends"
}


def test_get_folders(client):
    assert client.get("/api/v1/folders").status_code == 200


# def test_post_folder(client):
#     response = client.post("/api/v1/folders", data=folder)
#     assert response.status_code == 201
