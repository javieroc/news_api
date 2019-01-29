# Web Scrapper and Flask API

This is a simple web scrappper to get news from Salta city news. This news are exposed in
an API builded using flask.

## Prerequisites

You can run this project using Docker & Docker Compose. So in order to do that you should have installed both.

## How use it

Steps to run the scrapper and get up the API with news.

- Clone the project: `git clone git@github.com:javieroc/news_api.git`.
- Go to app directory: `cd news_api`.
- Get up the containers: `docker-compose up -d`.
- Go into the api container, check the container id running `docker ps`, and then `docker exec -it [container_id] bash`.
- Go to scrapper folder (this step inside container): `cd scrapper`.
- Populate mongo database using the scrapping script: `python script.py`. Wait to the script complete.
- You are able to exit from the container, just type exit.
- Done! Check your news in `http://localhost:3000/news`.

## License

MIT
