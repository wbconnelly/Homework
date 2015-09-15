"""OPTIONAL WEB SCRAPING HOMEWORK
First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)
For example, get_movie_info('tt0111161') should return:
{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}
Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.
Finally, convert that list into a DataFrame.
"""
from bs4 import BeautifulSoup
import requests
import lxml

id_list = ['tt0111161', 'tt0110912', 'tt0114709']
info_list = []

def new_dict(x):
    x = {}
    return x

movie_list = {}
for ids in id_list:

    r = requests.get('http://www.imdb.com/title/'+ids)
    b = BeautifulSoup(r.text, 'lxml')

    title = b.find(name = 'span', attrs = {'class': 'itemprop', 'itemprop':'name'}).text.strip()
    star_rating =  b.find(name = 'span', attrs = {'itemprop':'ratingValue'}).text.strip()
    description = b.find(name = 'p', attrs = {'itemprop':'description'}).text.strip()
    content_rating =  b.find(name = 'meta', attrs = {'itemprop':'contentRating'})['content']
    duration = b.find(name = 'time', attrs = {'itemprop':'duration'}).text.strip()
    info_list = [title, star_rating, description, content_rating, duration]

    title_info = ['title', 'star_rating', 'description', 'content_rating', 'duration']

    movie_dict = {}
    
    i = 0
    for item in title_info:
        movie_dict[item] = info_list[i]
        i += 1
    movie_list[title] = movie_dict


print movie_list['The Shawshank Redemption']
print movie_list['Pulp Fiction']
print movie_list['Toy Story']
