from flask import Flask, jsonify, request
from gnewsclient import gnewsclient

app = Flask(__name__)

# Fetch 'X' number of news articles
@app.route('/news/<int:max_results>', methods=['GET'])
def get_news(max_results):
    # Initialize GNews client
    client = gnewsclient.NewsClient(language='en', max_results=10)
    client.max_results = max_results
    news_items = client.get_news()
    return jsonify({'news': news_items})

# Find a news article with a specific title
@app.route('/news/title/<string:title>', methods=['GET'])
def find_news_by_title(title):
    # Initialize GNews client
    client = gnewsclient.NewsClient(language='en', max_results=10)
    news_items = client.get_news()
    # Filter news items by title
    matching_news = [n for n in news_items if title.lower() in n['title'].lower()]
    return jsonify({'news': matching_news})

# Find news articles by author
@app.route('/news/author/<string:author>', methods=['GET'])
def find_news_by_author(author):
    # Initialize GNews client
    client = gnewsclient.NewsClient(language='en', max_results=10)
    news_items = client.get_news()

    # Filter news items by author
    matching_news = [n for n in news_items if (author.lower() in n.get('source', '').lower()) or (author.lower() in n['title'].lower())]

    return jsonify({'news': matching_news})

# Search by keywords
@app.route('/news/search', methods=['GET'])
def search_news():
    # Initialize GNews client
    client = gnewsclient.NewsClient(language='en', max_results=10)
    query_param = request.args.get('q')
    client.query = query_param
    news_items = client.get_news()

    # Get keywords from query param
    keywords = query_param.lower().split()

    # Filter and sort news items based on keyword matches
    matching_news = []
    for news in news_items:
        # Check if any of the keywords are present in the title or description
        num_matches = sum([1 for k in keywords if k in news['title'].lower() or k in news.get('desc', '').lower()])
        if num_matches > 0:
            matching_news.append((news, num_matches))

    # Sort matching news by number of keyword matches in descending order
    sorted_news = [n[0] for n in sorted(matching_news, key=lambda x: x[1], reverse=True)]

    return jsonify({'news': sorted_news})


if __name__ == '__main__':
    app.run()
