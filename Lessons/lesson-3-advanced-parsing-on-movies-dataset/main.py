import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

movies = pd.read_csv('files/movies.csv', names=column_names, sep='|', na_values=['?'], dtype={'budget':'float'}, thousands=',', index_col=['movie_title'])
print(movies)