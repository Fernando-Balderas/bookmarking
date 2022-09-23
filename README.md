# Bookmarking

Bookmarking is a Bookmark manager similar to the one used in web browsers. This project consits of an API and all information is stored in a postgres database.

## Stack
- Python 3
- Flask 2
- PostgreSQL 14
- Docker CE 20.10.18

## Endpoints
- GET /api/v1/bookmarks: Get a list of bookmarks
- GET /api/v1/bookmarks/folders/:id: Get a list of bookmarks for a folder
- POST /api/v1/bookmarks: Create a new bookmark
- PUT /api/v1/bookmarks/:id: Update a bookmark
- DELETE /api/v1/bookmarks/:id: Delete a bookmark

- GET /api/v1/folders: Get a list of folders
- POST /api/v1/folders: Create a new folder
- PUT /api/v1/folders/:id: Update a folder
- DELETE /api/v1/folders/:id: Delete a folder

## Run the app
```bash
# first deploy the database container
cd api
docker compose up -d

# then run flask api with following command
cd src
flask --app app --debug run

# finally, test some endpoint with your prefered client, for example:
curl localhost:5000/api/v1/bookmarks
```

## Testing
```bash
pytest -Wignore
coverage run -m pytest -Wignore
```

## Use psql into container terminal (optional)
docker exec -ti bookmarking-bookmarking-db-1 psql -U postgres