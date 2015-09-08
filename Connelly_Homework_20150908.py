# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 20:26:16 2015

@author: William
"""

import matplotlib.pyplot as plt
import pandas as pd

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
imdb = pd.read_csv("imdb_1000.csv", header = 0, na_filter = True)
imdb.head()
imdb.isnull().sum()
# check the number of rows and columns
imdb.shape
    # Out[27]: (979, 6)

# check the data type of each column
imdb.dtypes
"""star_rating       float64
title              object
content_rating     object
genre              object
duration            int64
actors_list        object"""

# calculate the average movie duration
imdb.duration.mean()
    #  120.97957099080695


# sort the DataFrame by duration to find the shortest and longest movies
imdb[['title','duration']].sort('duration', ascending = False).head()
imdb[['title','duration']].sort('duration', ascending = False).tail()

# create a histogram of duration, choosing an "appropriate" number of bins
imdb.duration.plot(kind = 'hist', bins = 50)

# use a box plot to display that same data
imdb.duration.describe()
imdb.duration.plot(kind = 'box')


#INTERMEDIATE LEVEL

# count how many movies have each of the content ratings
imdb.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
ratings = imdb.content_rating.value_counts()
ratings.plot(kind= 'bar')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

imdb.content_rating = imdb.content_rating.replace({'NOT RATED':'UNRATED','APPROVED':'UNRATED',
                                 'PASSED':'UNRATED', 'GP':'UNRATED' })

# convert the following content ratings to "NC-17": X, TV-MA
imdb.content_rating = imdb.content_rating.replace({'X':'NC-17','TV-MA':'NC-17'})

# count the number of missing values in each column
imdb.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
imdb[imdb.content_rating.isnull() == True]
imdb.content_rating = imdb.content_rating.fillna('No Rating')

# calculate the average star rating for movies 2 hours or longer,
imdb_2hrs = imdb[imdb.duration >= 120]
imdb_2hrs.star_rating.mean()
    # 7.948898678414082

# and compare that with the average star rating for movies shorter than 2 hours
imdb_under_2hrs = imdb[imdb.duration < 120]
imdb_under_2hrs.star_rating.mean()
    #7.838666666666657

# use a visualization to detect whether there is a relationship between duration and star rating
imdb.plot(kind = 'scatter', x ='star_rating', y = 'duration')

# calculate the average duration for each genre
imdb_genre = imdb[['genre', 'duration']]
imdb_genre.groupby('genre').mean()
"""             duration
genre                
Action     126.485294
Adventure  134.840000
Animation   96.596774
Biography  131.844156
Comedy     107.602564
Crime      122.298387
Drama      126.539568
Family     107.500000
Fantasy    112.000000
Film-Noir   97.333333
History     66.000000
Horror     102.517241
Mystery    115.625000
Sci-Fi     109.000000
Thriller   114.200000
Western    136.666667"""


# visualize the relationship between content rating and duration
imdb_content = imdb[['content_rating', 'duration']]
imdb_content.groupby('content_rating').mean().plot(kind = 'bar')
# or


imdb_content['Rating_Index'] = imdb_content.content_rating.map({'G':1, 'PG':2, 'PG-13':3, 'R':4, 'TV-MA':5, 'NC-17': 6, 'X':7, 'UNRATED':0, 'No Rating':0})
imdb_content.groupby('Rating_Index').mean().plot(kind = 'bar')

# determine the top rated movie (by star rating) for each genre
genres = imdb.genre.unique()
for g in genres:
    df = imdb[imdb.genre == g]
    df = df[['genre','title','star_rating']].sort('star_rating', ascending = False)
    print df.iloc[0]

# check if th.ere are multiple movies with the same title, and if so, determine if they are actually duplicates
dup_lst = []
for i in range(0,len(imdb.title)):    
    title = imdb.title.pop(i)
    if title in imdb.title:
        dup_lst.append(title)

# calculate the average star rating for each genre, but only include genres with at least 10 movies



