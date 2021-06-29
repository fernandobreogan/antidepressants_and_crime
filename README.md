# Pipeline

Get playlist from Spotify API -> Processing -> Scrape lyriocs through google library -> Processing -> Sentiment analysis of the lyrics

Input: Spotify Playlist ID
Output: Sentiment analysis of every song on the playlist: metrics and (simple) visualization.


1. We get our client id/client secret
2. With that, we get our spotify tokens

3. We make API calls
4. We now have a dataframe
5. We enrich the dataframe with the lyrics

6. We create sentiment analysis code


https://developer.spotify.com/dashboard/applications


Resources

Spacy: https://realpython.com/sentiment-analysis-python/


NLTK: https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk