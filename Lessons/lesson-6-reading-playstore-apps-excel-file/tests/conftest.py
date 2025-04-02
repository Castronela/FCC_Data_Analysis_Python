import pytest
import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

@pytest.fixture
def playstore_df():	
	excel_file = pd.ExcelFile(data_url)
	playstore_df = excel_file.parse(usecols=['App', 'Rating', 'Installs', 'Genres', 'Last_Updated'], parse_dates=['Last_Updated'])
	return playstore_df.sort_values('Rating', ascending=False).head(25)
