import pytest
import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']

@pytest.fixture
def simpsons():
	return pd.read_csv('files/simpsons-episodes.tsv', 
					   sep='\t', 
					   parse_dates=['Air date'],
					   skiprows=4,
					   names=col_names,
					   na_values=['no_val'],
					   index_col=['Production code'],
					   usecols=['Title', 'Air date', 'Production code', 'IMDB rating'])
                          