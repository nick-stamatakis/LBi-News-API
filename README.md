# LBi-News-API

Here's a brief description of each method in the Flask API that I used:

get_news: This method fetches a specified number of news articles from the GNews API. The user can provide a number of articles to fetch (default is 10) and an optional topic for the articles (default is 'Top Stories'). The method sends a request to the GNews API, receives the response, and returns the relevant information from the response in JSON format.

get_news_by_title: This method searches for news articles with a specific title on the GNews API. The user can provide a title to search for, and the method sends a request to the GNews API, receives the response, and returns the relevant information from the response in JSON format.

get_news_by_author: This method searches for news articles written by a specific author on the GNews API. The user can provide an author to search for, and the method sends a request to the GNews API, receives the response, and returns the relevant information from the response in JSON format.

search_news: This method searches for news articles containing one or more keywords on the GNews API. The user can provide one or more keywords to search for, and the method sends a request to the GNews API, receives the response, and returns the relevant information from the response in JSON format.

All of these methods use a Redis cache to store previously fetched articles so that subsequent requests for the same articles are served from the cache rather than making a new request to the GNews API.
