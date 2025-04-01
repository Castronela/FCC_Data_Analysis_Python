import pytest
import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'content_rating', 'budget', 'title_year', 'imdb_score', 'genre']

@pytest.fixture
def movies():
	return pd.read_csv('files/movies.csv', skiprows=3, names=column_names, sep='|', na_values=['?'])

