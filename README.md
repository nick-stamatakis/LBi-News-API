# LBi-News-API

I used Python, the Flask package, and the GNews API to make my application.

Here's how the code works:

The Flask app is created with the name "app".

The first endpoint is "/news/int:max_results" which fetches a specified number of news articles from the GNewsClient library. The maximum number of results is passed as a URL parameter. The GNewsClient is initialized with a language parameter of 'en' and a default maximum number of 10 articles.

The second endpoint is "/news/title/string:title" which searches for news articles that contain a specified keyword in their title. The keyword is passed as a URL parameter. The GNewsClient is initialized and a list comprehension is used to filter news articles based on whether the specified keyword is present in the article's title. The resulting list of matching articles is returned as a JSON response.

The third endpoint is "/news/author/string:author" which searches for news articles that were written by a specific author or have the author's name mentioned in their title. The author's name is passed as a URL parameter. The GNewsClient is initialized and a list comprehension is used to filter news articles based on whether the specified author's name is present in either the article's source or its title. The resulting list of matching articles is returned as a JSON response.

The fourth endpoint is "/news/search" which searches for news articles containing one or more specified keywords in their title or description. The keywords are passed as a URL parameter. The GNewsClient is initialized and the query parameter is set to the value of the keywords parameter. A list comprehension is used to filter news articles based on whether any of the specified keywords are present in the article's title or description. The resulting list of matching articles is sorted by the number of keyword matches in descending order and returned as a JSON response.

The Flask app is run using the "app.run()" method.

To un the code, download the python file, run it, and use these urls as examples of the functionality of each method:
http://localhost:5000/news/5                        //Fetches 5 articles
http://localhost:5000/news/title/Jack               //Fetches articles with String 'Jack' in the title
http://localhost:5000/news/author/CNN               //Fetches articles with String 'CNN' as the author
http://localhost:5000/news/search?q=lawsuit         //Fetches articles based on the keyword 'lawsuit'

